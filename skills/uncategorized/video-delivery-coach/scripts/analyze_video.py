#!/usr/bin/env python3
"""
Video Delivery Coach - Analyze your video recordings before publishing.

Evaluates voice (pace, pitch, volume), facial expressions (emotions, eye contact),
and content (filler words, structure) to help improve your Hinglish YouTube delivery.

Usage:
    python analyze_video.py --video "/path/to/video.mp4"
    python analyze_video.py --video "/path/to/video.mp4" --full
    python analyze_video.py --video "/path/to/video.mp4" --voice-only
"""

import argparse
import json
import os
import sys
import tempfile
from datetime import datetime
from pathlib import Path
from typing import Optional

try:
    from rich.console import Console
    from rich.panel import Panel
    from rich.table import Table
    from rich.markdown import Markdown
    from rich.progress import Progress, SpinnerColumn, TextColumn
    RICH_AVAILABLE = True
except ImportError:
    RICH_AVAILABLE = False
    print("Note: Install 'rich' for better output: pip install rich")

try:
    from anthropic import Anthropic
    ANTHROPIC_AVAILABLE = True
except ImportError:
    ANTHROPIC_AVAILABLE = False
    print("Error: anthropic package required. Install with: pip install anthropic")
    sys.exit(1)

from dotenv import load_dotenv

# Load environment variables
env_path = Path(__file__).parent.parent.parent.parent.parent / ".env"
if env_path.exists():
    load_dotenv(env_path)

# Common filler words to detect
FILLER_WORDS = [
    "um", "uh", "like", "you know", "basically", "actually", "literally",
    "so", "well", "i mean", "kind of", "sort of", "right", "okay so"
]

# Hinglish-specific fillers
HINGLISH_FILLERS = [
    "matlab", "toh", "basically", "actually", "aisa hai ki"
]


class VideoDeliveryCoach:
    """Analyze video recordings to improve delivery."""

    def __init__(self):
        self.console = Console() if RICH_AVAILABLE else None
        self.client = None
        self._init_client()

        # Check for optional dependencies
        self.librosa_available = False
        self.whisper_available = False
        self.opencv_available = False
        self.deepface_available = False
        self.mediapipe_available = False

        self._check_dependencies()

    def _init_client(self):
        """Initialize Anthropic client."""
        api_key = os.getenv("ANTHROPIC_API_KEY")
        if not api_key:
            self._print_error("ANTHROPIC_API_KEY not found in environment")
            sys.exit(1)
        self.client = Anthropic(api_key=api_key)

    def _check_dependencies(self):
        """Check which optional dependencies are available."""
        try:
            import librosa
            self.librosa_available = True
        except ImportError:
            pass

        try:
            from faster_whisper import WhisperModel
            self.whisper_available = True
        except ImportError:
            pass

        try:
            import cv2
            self.opencv_available = True
        except ImportError:
            pass

        try:
            from deepface import DeepFace
            self.deepface_available = True
        except ImportError:
            pass

        try:
            import mediapipe
            self.mediapipe_available = True
        except ImportError:
            pass

    def _print(self, message: str, style: str = None):
        """Print with optional rich formatting."""
        if RICH_AVAILABLE and self.console:
            self.console.print(message, style=style)
        else:
            print(message)

    def _print_error(self, message: str):
        """Print error message."""
        self._print(f"[ERROR] {message}", "red bold")

    def _print_panel(self, content: str, title: str):
        """Print content in a panel."""
        if RICH_AVAILABLE and self.console:
            self.console.print(Panel(Markdown(content), title=title))
        else:
            print(f"\n{'='*60}")
            print(f"  {title}")
            print('='*60)
            print(content)
            print('='*60 + "\n")

    def analyze_voice(self, video_path: str) -> dict:
        """Analyze voice attributes from video."""

        if not self.librosa_available:
            return {
                "error": "librosa not available. Install with: pip install librosa moviepy faster-whisper"
            }

        import librosa
        import numpy as np

        try:
            from moviepy import VideoFileClip
        except ImportError:
            from moviepy.editor import VideoFileClip

        self._print("Extracting audio from video...", "yellow")

        # Extract audio to temp file
        with tempfile.NamedTemporaryFile(suffix='.mp3', delete=False) as temp_file:
            temp_audio_path = temp_file.name

        try:
            video_clip = VideoFileClip(video_path)
            audio_clip = video_clip.audio
            audio_clip.write_audiofile(temp_audio_path, verbose=False, logger=None)
            audio_clip.close()
            video_clip.close()

            self._print("Analyzing voice attributes...", "yellow")

            # Load audio with librosa
            y, sr = librosa.load(temp_audio_path, sr=16000)
            duration = librosa.get_duration(y=y, sr=sr)

            # Transcription
            transcription = ""
            if self.whisper_available:
                self._print("Transcribing audio...", "yellow")
                from faster_whisper import WhisperModel
                model = WhisperModel("small", device="cpu", compute_type="int8")
                segments, _ = model.transcribe(temp_audio_path)
                transcription = " ".join(segment.text for segment in segments).strip()

            # Calculate metrics
            words = transcription.split() if transcription else []
            speech_rate = len(words) / (duration / 60.0) if duration > 0 else 0

            # Pitch variation
            pitches, magnitudes = librosa.piptrack(y=y, sr=sr)
            pitch_values = pitches[magnitudes > np.median(magnitudes)]
            pitch_variation = float(np.std(pitch_values)) if pitch_values.size > 0 else 0

            # Volume consistency
            rms = librosa.feature.rms(y=y)[0]
            volume_consistency = float(np.std(rms))

            # Detect filler words
            filler_counts = {}
            transcript_lower = transcription.lower()
            for filler in FILLER_WORDS + HINGLISH_FILLERS:
                count = transcript_lower.count(filler)
                if count > 0:
                    filler_counts[filler] = count

            return {
                "duration_seconds": round(duration, 2),
                "transcription": transcription,
                "word_count": len(words),
                "speech_rate_wpm": round(speech_rate, 1),
                "pitch_variation": round(pitch_variation, 2),
                "volume_consistency": round(volume_consistency, 4),
                "filler_words": filler_counts,
                "total_filler_count": sum(filler_counts.values())
            }

        finally:
            # Clean up temp file
            if os.path.exists(temp_audio_path):
                os.remove(temp_audio_path)

    def analyze_facial(self, video_path: str) -> dict:
        """Analyze facial expressions from video."""

        if not all([self.opencv_available, self.deepface_available, self.mediapipe_available]):
            missing = []
            if not self.opencv_available:
                missing.append("opencv-python")
            if not self.deepface_available:
                missing.append("deepface tf-keras")
            if not self.mediapipe_available:
                missing.append("mediapipe")
            return {
                "error": f"Missing dependencies: {', '.join(missing)}. Install with pip."
            }

        import cv2
        import numpy as np
        import mediapipe as mp
        from deepface import DeepFace

        self._print("Analyzing facial expressions...", "yellow")

        mp_face_mesh = mp.solutions.face_mesh
        face_mesh = mp_face_mesh.FaceMesh(static_image_mode=False, max_num_faces=1)
        cap = cv2.VideoCapture(video_path)

        emotion_timeline = []
        eye_contact_count = 0
        smile_count = 0
        frame_count = 0
        fps = cap.get(cv2.CAP_PROP_FPS)

        # Process every nth frame for performance
        frame_interval = 10  # Analyze every 10th frame

        try:
            while cap.isOpened():
                ret, frame = cap.read()
                if not ret:
                    break

                frame_count += 1
                if frame_count % frame_interval != 0:
                    continue

                # Resize for faster processing
                frame = cv2.resize(frame, (640, 480))
                rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                results = face_mesh.process(rgb_frame)

                if results.multi_face_landmarks:
                    for face_landmarks in results.multi_face_landmarks:
                        landmarks = face_landmarks.landmark
                        h, w, _ = frame.shape
                        landmark_coords = [(int(lm.x * w), int(lm.y * h)) for lm in landmarks]

                        # Emotion detection
                        try:
                            analysis = DeepFace.analyze(frame, actions=['emotion'], enforce_detection=False)
                            emotion = analysis[0]['dominant_emotion']
                            if emotion == "happy":
                                smile_count += 1

                            timestamp = round(frame_count / fps, 2)
                            emotion_timeline.append({"timestamp": timestamp, "emotion": emotion})
                        except Exception:
                            continue

                        # Eye contact estimation
                        try:
                            left_eye_upper = landmark_coords[159]
                            left_eye_lower = landmark_coords[145]
                            right_eye_upper = landmark_coords[386]
                            right_eye_lower = landmark_coords[374]

                            left_opening = np.linalg.norm(np.array(left_eye_upper) - np.array(left_eye_lower))
                            right_opening = np.linalg.norm(np.array(right_eye_upper) - np.array(right_eye_lower))
                            avg_opening = (left_opening + right_opening) / 2

                            if avg_opening > 5:
                                eye_contact_count += 1
                        except Exception:
                            continue

        finally:
            cap.release()
            face_mesh.close()

        total_processed = frame_count // frame_interval
        if total_processed == 0:
            total_processed = 1

        # Summarize emotion timeline
        emotion_summary = {}
        for entry in emotion_timeline:
            emotion = entry['emotion']
            emotion_summary[emotion] = emotion_summary.get(emotion, 0) + 1

        dominant_emotion = max(emotion_summary, key=emotion_summary.get) if emotion_summary else "unknown"

        return {
            "frames_analyzed": total_processed,
            "eye_contact_frequency": round(eye_contact_count / total_processed, 2),
            "smile_frequency": round(smile_count / total_processed, 2),
            "emotion_distribution": emotion_summary,
            "dominant_emotion": dominant_emotion,
            "emotion_timeline_sample": emotion_timeline[:10]  # First 10 entries
        }

    def generate_coaching_report(self, voice_data: dict, facial_data: dict = None, video_path: str = "") -> str:
        """Generate comprehensive coaching report using Claude."""

        # Build analysis summary
        analysis_text = f"""
VIDEO ANALYSIS DATA:

File: {os.path.basename(video_path)}

VOICE ANALYSIS:
- Duration: {voice_data.get('duration_seconds', 'N/A')} seconds
- Word Count: {voice_data.get('word_count', 'N/A')}
- Speech Rate: {voice_data.get('speech_rate_wpm', 'N/A')} WPM (Target: 120-160)
- Pitch Variation: {voice_data.get('pitch_variation', 'N/A')} Hz (Higher = more engaging)
- Volume Consistency: {voice_data.get('volume_consistency', 'N/A')} (Lower = more consistent)
- Filler Words: {json.dumps(voice_data.get('filler_words', {}), indent=2)}
- Total Filler Count: {voice_data.get('total_filler_count', 0)}

TRANSCRIPTION:
{voice_data.get('transcription', 'Not available')[:2000]}...
"""

        if facial_data and 'error' not in facial_data:
            analysis_text += f"""

FACIAL ANALYSIS:
- Eye Contact Frequency: {facial_data.get('eye_contact_frequency', 'N/A')} (Target: >0.6)
- Smile Frequency: {facial_data.get('smile_frequency', 'N/A')} (Target: >0.3)
- Dominant Emotion: {facial_data.get('dominant_emotion', 'N/A')}
- Emotion Distribution: {json.dumps(facial_data.get('emotion_distribution', {}), indent=2)}
"""

        prompt = f"""You are a video delivery coach for Dr. Shailesh Singh, an interventional cardiologist
who creates Hinglish YouTube content (70% Hindi, 30% English) about cardiology.

Analyze this video recording data and provide coaching feedback.

{analysis_text}

Provide your analysis in this format:

## QUICK SUMMARY
[One-line assessment]

## SCORES (1-5 each)
| Dimension | Score | Notes |
|-----------|-------|-------|
| Content & Organization | X/5 | Brief note |
| Delivery & Vocal Quality | X/5 | Brief note |
| Body Language & Eye Contact | X/5 | Brief note |
| Audience Engagement | X/5 | Brief note |
| Language & Clarity | X/5 | Brief note |

**Total: XX/25** - [Interpretation: Needs improvement / Developing / Competent / Proficient / Outstanding]

## TOP 3 STRENGTHS
1. [Specific strength]
2. [Specific strength]
3. [Specific strength]

## TOP 3 IMPROVEMENTS NEEDED
1. [Specific improvement with actionable advice]
2. [Specific improvement with actionable advice]
3. [Specific improvement with actionable advice]

## HINGLISH-SPECIFIC FEEDBACK
- Code-switching: [Assessment]
- Cultural engagement phrases: [Assessment]
- Pace for technical terms: [Assessment]

## FILLER WORD ACTION PLAN
[Specific advice for reducing the most common fillers]

## NEXT VIDEO FOCUS
[One key thing to focus on in the next recording]

Be specific, actionable, and encouraging. Focus on improvement, not criticism.
"""

        response = self.client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=2000,
            messages=[{"role": "user", "content": prompt}]
        )

        return response.content[0].text

    def analyze(self, video_path: str, full_mode: bool = False, voice_only: bool = False) -> str:
        """Run complete video analysis."""

        if not os.path.exists(video_path):
            return f"Error: Video file not found: {video_path}"

        self._print(f"\nAnalyzing: {os.path.basename(video_path)}", "cyan bold")
        self._print("=" * 50)

        # Voice analysis (always run)
        voice_data = self.analyze_voice(video_path)
        if 'error' in voice_data:
            self._print(f"Voice analysis error: {voice_data['error']}", "red")
            voice_data = {}
        else:
            self._print("✓ Voice analysis complete", "green")

        # Facial analysis (only if full mode and not voice-only)
        facial_data = None
        if full_mode and not voice_only:
            facial_data = self.analyze_facial(video_path)
            if 'error' in facial_data:
                self._print(f"Facial analysis skipped: {facial_data['error']}", "yellow")
                facial_data = None
            else:
                self._print("✓ Facial analysis complete", "green")
        elif not voice_only:
            self._print("Skipping facial analysis (use --full for complete analysis)", "yellow")

        # Generate coaching report
        self._print("Generating coaching report...", "yellow")
        report = self.generate_coaching_report(voice_data, facial_data, video_path)
        self._print("✓ Report generated", "green")

        return report


def main():
    parser = argparse.ArgumentParser(
        description="Analyze video recordings to improve delivery"
    )

    parser.add_argument(
        "--video", "-v",
        type=str,
        required=True,
        help="Path to video file (MP4, MOV, AVI, MKV)"
    )

    parser.add_argument(
        "--full", "-f",
        action="store_true",
        help="Full analysis including facial expressions (requires OpenCV, DeepFace, Mediapipe)"
    )

    parser.add_argument(
        "--voice-only",
        action="store_true",
        help="Voice analysis only (faster, lighter dependencies)"
    )

    parser.add_argument(
        "--output", "-o",
        type=str,
        help="Output directory for report"
    )

    args = parser.parse_args()

    coach = VideoDeliveryCoach()

    # Check dependencies
    print("\nDependency Status:")
    print(f"  - librosa: {'✓' if coach.librosa_available else '✗'}")
    print(f"  - faster-whisper: {'✓' if coach.whisper_available else '✗'}")
    print(f"  - opencv: {'✓' if coach.opencv_available else '✗'}")
    print(f"  - deepface: {'✓' if coach.deepface_available else '✗'}")
    print(f"  - mediapipe: {'✓' if coach.mediapipe_available else '✗'}")
    print()

    if not coach.librosa_available:
        print("ERROR: librosa is required for voice analysis.")
        print("Install with: pip install librosa moviepy faster-whisper")
        sys.exit(1)

    # Run analysis
    report = coach.analyze(
        args.video,
        full_mode=args.full,
        voice_only=args.voice_only
    )

    # Output report
    coach._print_panel(report, "VIDEO DELIVERY COACHING REPORT")

    # Save to file if output specified
    if args.output:
        output_dir = Path(args.output)
        output_dir.mkdir(parents=True, exist_ok=True)

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        video_name = Path(args.video).stem
        filename = f"video_coaching_{video_name}_{timestamp}.md"
        output_path = output_dir / filename

        with open(output_path, "w") as f:
            f.write(f"# Video Delivery Coaching Report\n\n")
            f.write(f"**Video:** {os.path.basename(args.video)}\n")
            f.write(f"**Analyzed:** {datetime.now().isoformat()}\n\n")
            f.write("---\n\n")
            f.write(report)

        print(f"\nReport saved to: {output_path}")


if __name__ == "__main__":
    main()
