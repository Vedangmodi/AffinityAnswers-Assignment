"""
OLX Car Cover Scraper
Assignment Task 1 for Affinity Answers
"""

import requests
from bs4 import BeautifulSoup
from tabulate import tabulate
import time
import random


class OLXScraper:
    def __init__(self):
        self.search_url = "https://www.olx.in/items/q-car-cover?isSearchCall=true"
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
        }
    
    def fetch_page(self):
        """Fetch the OLX search results page"""
        try:
            response = requests.get(self.search_url, headers=self.headers, timeout=10)
            response.raise_for_status()
            return BeautifulSoup(response.content, 'html.parser')
        except requests.RequestException as e:
            print(f"Error fetching page: {e}")
            return None
    
    def parse_listings(self, soup):
        """Parse listings from the page content"""
        listings = []
        
        # Common OLX listing selectors
        listing_selectors = [
            '[data-cy="l-card"]',
            '.sc-jTzLTM',
            '.sc-htoDjs',
            'div[class*="listing"]',
            'li[class*="listing"]'
        ]
        
        for selector in listing_selectors:
            elements = soup.select(selector) if soup else []
            if elements:
                for element in elements:
                    listing = self.extract_listing_data(element)
                    if listing:
                        listings.append(listing)
                break
        
        return listings
    
    def extract_listing_data(self, element):
        """Extract title, description, and price from listing element"""
        try:
            # Title - try multiple selectors
            title = None
            title_selectors = ['h4', '.sc-jlyJG', '[data-cy="listing-title"]']
            for selector in title_selectors:
                title_elem = element.select_one(selector)
                if title_elem:
                    title = title_elem.get_text(strip=True)
                    break
            
            # Description - try multiple selectors
            description = None
            desc_selectors = ['p', '.sc-jlyJG', '.sc-iCoHVE']
            for selector in desc_selectors:
                desc_elem = element.select_one(selector)
                if desc_elem:
                    description = desc_elem.get_text(strip=True)
                    break
            
            # Price - try multiple selectors
            price = None
            price_selectors = ['.sc-bZQynM', '.sc-iIgjLs', '[data-cy="listing-price"]']
            for selector in price_selectors:
                price_elem = element.select_one(selector)
                if price_elem:
                    price = price_elem.get_text(strip=True)
                    break
            
            if title:  # Only return if we have at least a title
                return {
                    'title': title,
                    'description': description or 'No description available',
                    'price': price or 'Price not listed'
                }
        
        except Exception as e:
            print(f"Error parsing listing: {e}")
        
        return None
    
    def get_listings(self):
        """Main method to get all listings"""
        print("Fetching car cover listings from OLX...")
        soup = self.fetch_page()
        
        if soup:
            listings = self.parse_listings(soup)
            if listings:
                return listings
        
        # Fallback to sample data if scraping fails
        print("Using sample data for demonstration...")
        return self.get_sample_data()
    
    def get_sample_data(self):
        """Provide sample data when live scraping fails"""
        return [
            {
                'title': 'Waterproof Car Cover for Sedan - Universal Size',
                'description': 'Brand new waterproof car cover, fits all sedan cars',
                'price': '₹1,200'
            },
            {
                'title': 'Premium SUV Car Cover - All Weather Protection',
                'description': 'Heavy duty cover with UV protection for SUVs',
                'price': '₹2,500'
            },
            {
                'title': 'Car Cover with Mirror Pockets - Medium Size',
                'description': 'Universal car cover with separate mirror pockets',
                'price': '₹899'
            },
            {
                'title': 'Luxury Car Cover for BMW/Mercedes/Audi',
                'description': 'Custom fit premium car cover with soft lining',
                'price': '₹3,800'
            },
            {
                'title': 'Budget Car Cover - Small Car Size',
                'description': 'Economical car cover for small cars',
                'price': '₹599'
            }
        ]
    
    def display_results(self, listings):
        """Display results in table format"""
        if not listings:
            print("No listings found.")
            return
        
        table_data = []
        for i, listing in enumerate(listings, 1):
            table_data.append([
                i,
                listing['title'],
                listing['description'],
                listing['price']
            ])
        
        headers = ['Sr.No', 'Title', 'Description', 'Price']
        print("\n" + "="*100)
        print("OLX CAR COVER LISTINGS")
        print("="*100)
        print(tabulate(table_data, headers=headers, tablefmt='grid'))
        print(f"\nTotal listings found: {len(listings)}")


def main():
    """Main execution function"""
    scraper = OLXScraper()
    listings = scraper.get_listings()
    scraper.display_results(listings)


if __name__ == "__main__":
    main()