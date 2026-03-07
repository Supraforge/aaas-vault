import { useState, useEffect } from "react";
import { InstagramCarousel } from "./components/InstagramCarousel";
import { BPCarousel } from "./components/BPCarousel";
import { FluCarousel } from "./components/FluCarousel";
import { BellyFatCarousel } from "./components/BellyFatCarousel";
import { SugarCarousel } from "./components/SugarCarousel";
import { FoodCholesterolCarousel } from "./components/FoodCholesterolCarousel";
import { BP120Carousel } from "./components/BP120Carousel";
import { RestaurantCarousel } from "./components/RestaurantCarousel";
import { VitaminDCarousel } from "./components/VitaminDCarousel";
import { BPMonitorCarousel } from "./components/BPMonitorCarousel";
import { ProteinCarousel } from "./components/ProteinCarousel";
import { DetoxCarousel } from "./components/DetoxCarousel";
import { BlankTemplateCarousel } from "./components/BlankTemplateCarousel";
import { FooterBanner } from "./components/FooterBanner";
import { RenderPage } from "./components/RenderPage";
import { Button } from "./components/ui/button";

export default function App() {
  // Check if we're in render mode (for Puppeteer)
  const params = new URLSearchParams(window.location.search);
  const isRenderMode = params.get('mode') === 'render';

  if (isRenderMode) {
    return <RenderPage />;
  }
  const [activeSeries, setActiveSeries] = useState<
    "cholesterol" | "bp" | "flu" | "bellyfat" | "sugar" | "foodcholesterol" | "bp120" | "restaurant" | "vitamind" | "bpmonitor" | "protein" | "detox" | "blank" | "footer"
  >("footer");

  return (
    <div className="w-full">
      {/* Series selector */}
      <div className="fixed top-6 left-1/2 transform -translate-x-1/2 z-50 flex gap-3 bg-slate-800/90 backdrop-blur-sm p-3 rounded-full shadow-2xl border border-white/10">
        <Button
          onClick={() => setActiveSeries("cholesterol")}
          className={`rounded-full px-6 ${
            activeSeries === "cholesterol"
              ? "bg-gradient-to-r from-[#207178] to-[#F28C81]"
              : "bg-white/10 hover:bg-white/20"
          }`}
          style={{
            fontFamily: "Inter, sans-serif",
            fontSize: "16px",
            fontWeight: 600,
          }}
        >
          Cholesterol Series
        </Button>
        <Button
          onClick={() => setActiveSeries("bp")}
          className={`rounded-full px-6 ${
            activeSeries === "bp"
              ? "bg-gradient-to-r from-[#E63946] to-[#F28C81]"
              : "bg-white/10 hover:bg-white/20"
          }`}
          style={{
            fontFamily: "Inter, sans-serif",
            fontSize: "16px",
            fontWeight: 600,
          }}
        >
          Blood Pressure Series
        </Button>
        <Button
          onClick={() => setActiveSeries("flu")}
          className={`rounded-full px-6 ${
            activeSeries === "flu"
              ? "bg-gradient-to-r from-[#207178] to-[#E63946]"
              : "bg-white/10 hover:bg-white/20"
          }`}
          style={{
            fontFamily: "Inter, sans-serif",
            fontSize: "16px",
            fontWeight: 600,
          }}
        >
          Influenza Series
        </Button>
        <Button
          onClick={() => setActiveSeries("bellyfat")}
          className={`rounded-full px-6 ${
            activeSeries === "bellyfat"
              ? "bg-gradient-to-r from-[#F28C81] to-[#E63946]"
              : "bg-white/10 hover:bg-white/20"
          }`}
          style={{
            fontFamily: "Inter, sans-serif",
            fontSize: "16px",
            fontWeight: 600,
          }}
        >
          Belly Fat Series
        </Button>
        <Button
          onClick={() => setActiveSeries("sugar")}
          className={`rounded-full px-6 ${
            activeSeries === "sugar"
              ? "bg-gradient-to-r from-[#F28C81] to-[#E63946]"
              : "bg-white/10 hover:bg-white/20"
          }`}
          style={{
            fontFamily: "Inter, sans-serif",
            fontSize: "16px",
            fontWeight: 600,
          }}
        >
          Sugar Series
        </Button>
        <Button
          onClick={() => setActiveSeries("foodcholesterol")}
          className={`rounded-full px-6 ${
            activeSeries === "foodcholesterol"
              ? "bg-gradient-to-r from-[#F28C81] to-[#E63946]"
              : "bg-white/10 hover:bg-white/20"
          }`}
          style={{
            fontFamily: "Inter, sans-serif",
            fontSize: "16px",
            fontWeight: 600,
          }}
        >
          Food Cholesterol Series
        </Button>
        <Button
          onClick={() => setActiveSeries("bp120")}
          className={`rounded-full px-6 ${
            activeSeries === "bp120"
              ? "bg-gradient-to-r from-[#F28C81] to-[#E63946]"
              : "bg-white/10 hover:bg-white/20"
          }`}
          style={{
            fontFamily: "Inter, sans-serif",
            fontSize: "16px",
            fontWeight: 600,
          }}
        >
          BP 120 Series
        </Button>
        <Button
          onClick={() => setActiveSeries("restaurant")}
          className={`rounded-full px-6 ${
            activeSeries === "restaurant"
              ? "bg-gradient-to-r from-[#F28C81] to-[#E63946]"
              : "bg-white/10 hover:bg-white/20"
          }`}
          style={{
            fontFamily: "Inter, sans-serif",
            fontSize: "16px",
            fontWeight: 600,
          }}
        >
          Restaurant Series
        </Button>
        <Button
          onClick={() => setActiveSeries("vitamind")}
          className={`rounded-full px-6 ${
            activeSeries === "vitamind"
              ? "bg-gradient-to-r from-[#F28C81] to-[#E63946]"
              : "bg-white/10 hover:bg-white/20"
          }`}
          style={{
            fontFamily: "Inter, sans-serif",
            fontSize: "16px",
            fontWeight: 600,
          }}
        >
          Vitamin D Series
        </Button>
        <Button
          onClick={() => setActiveSeries("bpmonitor")}
          className={`rounded-full px-6 ${
            activeSeries === "bpmonitor"
              ? "bg-gradient-to-r from-[#F28C81] to-[#E63946]"
              : "bg-white/10 hover:bg-white/20"
          }`}
          style={{
            fontFamily: "Inter, sans-serif",
            fontSize: "16px",
            fontWeight: 600,
          }}
        >
          BP Monitor Series
        </Button>
        <Button
          onClick={() => setActiveSeries("protein")}
          className={`rounded-full px-6 ${
            activeSeries === "protein"
              ? "bg-gradient-to-r from-[#F28C81] to-[#E63946]"
              : "bg-white/10 hover:bg-white/20"
          }`}
          style={{
            fontFamily: "Inter, sans-serif",
            fontSize: "16px",
            fontWeight: 600,
          }}
        >
          Protein Series
        </Button>
        <Button
          onClick={() => setActiveSeries("detox")}
          className={`rounded-full px-6 ${
            activeSeries === "detox"
              ? "bg-gradient-to-r from-[#F28C81] to-[#E63946]"
              : "bg-white/10 hover:bg-white/20"
          }`}
          style={{
            fontFamily: "Inter, sans-serif",
            fontSize: "16px",
            fontWeight: 600,
          }}
        >
          Detox Series
        </Button>
        <Button
          onClick={() => setActiveSeries("blank")}
          className={`rounded-full px-6 ${
            activeSeries === "blank"
              ? "bg-gradient-to-r from-[#F28C81] to-[#E63946]"
              : "bg-white/10 hover:bg-white/20"
          }`}
          style={{
            fontFamily: "Inter, sans-serif",
            fontSize: "16px",
            fontWeight: 600,
          }}
        >
          Blank Templates
        </Button>
        <Button
          onClick={() => setActiveSeries("footer")}
          className={`rounded-full px-6 ${
            activeSeries === "footer"
              ? "bg-gradient-to-r from-[#207178] to-[#E4F1EF]"
              : "bg-white/10 hover:bg-white/20"
          }`}
          style={{
            fontFamily: "Inter, sans-serif",
            fontSize: "16px",
            fontWeight: 600,
          }}
        >
          Footer Banner
        </Button>
      </div>

      {/* Active carousel */}
      {activeSeries === "cholesterol" ? (
        <InstagramCarousel />
      ) : activeSeries === "bp" ? (
        <BPCarousel />
      ) : activeSeries === "flu" ? (
        <FluCarousel />
      ) : activeSeries === "bellyfat" ? (
        <BellyFatCarousel />
      ) : activeSeries === "sugar" ? (
        <SugarCarousel />
      ) : activeSeries === "foodcholesterol" ? (
        <FoodCholesterolCarousel />
      ) : activeSeries === "bp120" ? (
        <BP120Carousel />
      ) : activeSeries === "restaurant" ? (
        <RestaurantCarousel />
      ) : activeSeries === "vitamind" ? (
        <VitaminDCarousel />
      ) : activeSeries === "bpmonitor" ? (
        <BPMonitorCarousel />
      ) : activeSeries === "protein" ? (
        <ProteinCarousel />
      ) : activeSeries === "detox" ? (
        <DetoxCarousel />
      ) : activeSeries === "blank" ? (
        <BlankTemplateCarousel />
      ) : (
        <FooterBanner />
      )}
    </div>
  );
}