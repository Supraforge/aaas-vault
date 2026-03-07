#!/usr/bin/env python3
"""
CE Research Tool - Brand Voice Forensics
Gathers: tone, style, messages, examples, templates
Sources: website copy, blog, social posts, press releases, marketing
"""

from research_base import (
    create_research_parser,
    load_prompts,
    generate_research_prompt,
    save_research,
    get_output_dir
)


def main():
    parser = create_research_parser(
        "brand",
        "Research brand voice forensics - tone, style, messaging"
    )
    args = parser.parse_args()

    prompts = load_prompts()
    config = prompts['research_dimensions']['brand']

    if args.generate_prompt:
        prompt = generate_research_prompt(args.company, 'brand', config)
        print(prompt)
        print("\n" + "="*60)
        print("INSTRUCTIONS: Execute the searches above, then save results to:")
        output_dir = get_output_dir(args.company)
        print(f"  {output_dir / 'research' / 'brand.md'}")
    else:
        print(f"CE Research - Brand Voice Forensics for: {args.company}")
        print("="*60)
        print("\nTo generate the research prompt, run with --generate-prompt flag:")
        print(f"  python run.py research_brand.py --company '{args.company}' --generate-prompt")
        print("\nOr manually execute web searches for:")
        for query in config['search_queries']:
            formatted = query.replace('{company}', args.company)
            print(f"  - {formatted}")


if __name__ == "__main__":
    main()
