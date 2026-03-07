#!/usr/bin/env python3
"""
CE Research Tool - Company Snapshot
Gathers: overview, product, features, use-cases, audience, proof, positioning, voice, pricing
Sources: website, social, PR, reviews, interviews, aggregators
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
        "company",
        "Research company snapshot - overview, product, features, positioning"
    )
    args = parser.parse_args()

    prompts = load_prompts()
    config = prompts['research_dimensions']['company']

    if args.generate_prompt:
        # Generate prompt for Claude to execute
        prompt = generate_research_prompt(args.company, 'company', config)
        print(prompt)
        print("\n" + "="*60)
        print("INSTRUCTIONS: Execute the searches above, then save results to:")
        output_dir = get_output_dir(args.company)
        print(f"  {output_dir / 'research' / 'company.md'}")
    else:
        # Interactive mode - print instructions
        print(f"CE Research - Company Snapshot for: {args.company}")
        print("="*60)
        print("\nTo generate the research prompt, run with --generate-prompt flag:")
        print(f"  python run.py research_company.py --company '{args.company}' --generate-prompt")
        print("\nOr manually execute web searches for:")
        for query in config['search_queries']:
            formatted = query.replace('{company}', args.company)
            print(f"  - {formatted}")


if __name__ == "__main__":
    main()
