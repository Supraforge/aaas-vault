#!/usr/bin/env python3
"""
CE Research Tool - Market Intelligence
Gathers: market definition, trends, size, insights, gap analysis
Sources: industry reports, analyst coverage, news, market research
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
        "market",
        "Research market intelligence - trends, size, insights"
    )
    args = parser.parse_args()

    prompts = load_prompts()
    config = prompts['research_dimensions']['market']

    if args.generate_prompt:
        prompt = generate_research_prompt(args.company, 'market', config)
        print(prompt)
        print("\n" + "="*60)
        print("INSTRUCTIONS: Execute the searches above, then save results to:")
        output_dir = get_output_dir(args.company)
        print(f"  {output_dir / 'research' / 'market.md'}")
    else:
        print(f"CE Research - Market Intelligence for: {args.company}")
        print("="*60)
        print("\nTo generate the research prompt, run with --generate-prompt flag:")
        print(f"  python run.py research_market.py --company '{args.company}' --generate-prompt")
        print("\nOr manually execute web searches for:")
        for query in config['search_queries']:
            formatted = query.replace('{company}', args.company).replace('{industry}', f'{args.company} industry')
            print(f"  - {formatted}")


if __name__ == "__main__":
    main()
