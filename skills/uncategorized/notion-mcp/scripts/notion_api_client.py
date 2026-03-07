#!/usr/bin/env python3
"""
Notion API Client for Python
"""
import os
import json
from notion_client import Client
from dotenv import load_dotenv

load_dotenv()

class NotionAPIClient:
    def __init__(self):
        token = os.getenv('NOTION_API_TOKEN')
        if not token:
            raise ValueError('NOTION_API_TOKEN not found in environment variables')
        self.client = Client(auth=token)
    
    def query_database(self, database_id, filter_obj=None, sorts=None):
        """Query a Notion database"""
        try:
            response = self.client.databases.query(
                database_id=database_id,
                filter=filter_obj,
                sorts=sorts
            )
            return response
        except Exception as e:
            return {'error': str(e)}
    
    def create_page(self, parent_database_id, properties, children=None):
        """Create a new page in a database"""
        try:
            response = self.client.pages.create(
                parent={'database_id': parent_database_id},
                properties=properties,
                children=children or []
            )
            return response
        except Exception as e:
            return {'error': str(e)}
    
    def update_page(self, page_id, properties):
        """Update an existing page"""
        try:
            response = self.client.pages.update(
                page_id=page_id,
                properties=properties
            )
            return response
        except Exception as e:
            return {'error': str(e)}
    
    def retrieve_page(self, page_id):
        """Retrieve a page by ID"""
        try:
            response = self.client.pages.retrieve(page_id=page_id)
            return response
        except Exception as e:
            return {'error': str(e)}
    
    def search(self, query=''):
        """Search across Notion"""
        try:
            response = self.client.search(
                query=query,
                sort={
                    'direction': 'descending',
                    'timestamp': 'last_edited_time'
                }
            )
            return response
        except Exception as e:
            return {'error': str(e)}
    
    def export_page_to_markdown(self, page_id, output_file=None):
        """Export a page to markdown format"""
        try:
            # Get page content
            page = self.retrieve_page(page_id)
            if 'error' in page:
                return page
            
            # Get page blocks
            blocks = self.client.blocks.children.list(block_id=page_id)
            
            # Convert to markdown (simplified)
            markdown = f"# {page.get('properties', {}).get('title', {}).get('title', [{}])[0].get('text', {}).get('content', 'Untitled')}\n\n"
            
            for block in blocks.get('results', []):
                block_type = block.get('type')
                if block_type == 'paragraph':
                    text = block.get('paragraph', {}).get('text', [])
                    if text:
                        content = ''.join([t.get('text', {}).get('content', '') for t in text])
                        markdown += f"{content}\n\n"
                elif block_type == 'heading_1':
                    text = block.get('heading_1', {}).get('text', [])
                    if text:
                        content = ''.join([t.get('text', {}).get('content', '') for t in text])
                        markdown += f"# {content}\n\n"
                elif block_type == 'heading_2':
                    text = block.get('heading_2', {}).get('text', [])
                    if text:
                        content = ''.join([t.get('text', {}).get('content', '') for t in text])
                        markdown += f"## {content}\n\n"
                elif block_type == 'bulleted_list_item':
                    text = block.get('bulleted_list_item', {}).get('text', [])
                    if text:
                        content = ''.join([t.get('text', {}).get('content', '') for t in text])
                        markdown += f"* {content}\n"
                elif block_type == 'numbered_list_item':
                    text = block.get('numbered_list_item', {}).get('text', [])
                    if text:
                        content = ''.join([t.get('text', {}).get('content', '') for t in text])
                        markdown += f"1. {content}\n"
                elif block_type == 'code':
                    text = block.get('code', {}).get('text', [])
                    language = block.get('code', {}).get('language', '')
                    if text:
                        content = ''.join([t.get('text', {}).get('content', '') for t in text])
                        markdown += f"```{language}\n{content}\n```\n\n"
            
            if output_file:
                with open(output_file, 'w', encoding='utf-8') as f:
                    f.write(markdown)
                return {'success': True, 'file': output_file, 'content': markdown[:500] + '...'}
            
            return {'success': True, 'content': markdown}
        except Exception as e:
            return {'error': str(e)}

if __name__ == '__main__':
    # Example usage
    client = NotionAPIClient()
    
    # Example: Search for pages
    results = client.search('API documentation')
    print(json.dumps(results, indent=2))
