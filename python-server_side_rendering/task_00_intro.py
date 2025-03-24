#!/usr/bin/env python3
"""
Task 0: Creating a Simple Templating Program
This module provides functionality to generate personalized invitation files
from a template with placeholders and a list of objects.
"""

import os
import logging
from typing import List, Dict, Any

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def generate_invitations(template: str, attendees: List[Dict[str, Any]]) -> None:
    """
    Generate personalized invitation files from a template and list of attendees.
    
    Args:
        template (str): The template string with placeholders
        attendees (List[Dict[str, Any]]): List of dictionaries containing attendee information
    
    Returns:
        None
    
    Raises:
        None (uses logging for error reporting)
    """
    # Input validation
    if not isinstance(template, str):
        logger.error("Template must be a string")
        return
    
    if not isinstance(attendees, list):
        logger.error("Attendees must be a list")
        return
    
    if not template.strip():
        logger.error("Template is empty, no output files generated.")
        return
    
    if not attendees:
        logger.error("No data provided, no output files generated.")
        return
    
    # Process each attendee
    for index, attendee in enumerate(attendees, 1):
        if not isinstance(attendee, dict):
            logger.error(f"Invalid attendee data type at index {index}")
            continue
            
        # Create personalized content
        personalized_content = template
        
        # Replace placeholders with values or N/A
        for key in ['name', 'event_title', 'event_date', 'event_location']:
            value = attendee.get(key, 'N/A')
            placeholder = '{' + key + '}'
            personalized_content = personalized_content.replace(placeholder, str(value))
        
        # Generate output filename
        output_file = f'output_{index}.txt'
        
        try:
            # Write to file
            with open(output_file, 'w') as f:
                f.write(personalized_content)
            logger.info(f"Generated invitation file: {output_file}")
        except IOError as e:
            logger.error(f"Error writing file {output_file}: {str(e)}")

if __name__ == "__main__":
    # Example usage
    with open('template.txt', 'r') as file:
        template_content = file.read()

    # Example attendees data
    attendees = [
        {"name": "Alice", "event_title": "Python Conference", "event_date": "2023-07-15", "event_location": "New York"},
        {"name": "Bob", "event_title": "Data Science Workshop", "event_date": "2023-08-20", "event_location": "San Francisco"},
        {"name": "Charlie", "event_title": "AI Summit", "event_date": None, "event_location": "Boston"}
    ]

    # Generate invitations
    generate_invitations(template_content, attendees) 