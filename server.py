from fastmcp import FastMCP
from textblob import TextBlob

# Create an MCP server
mcp = FastMCP("Weather Service")


@mcp.tool()
def get_weather(location: str) -> str:
    """Get the current weather for a specified location."""
    return f"Weather in {location}: Sunny, 72°F"

@mcp.tool()
def sentiment_analysis(text: str) -> dict:
    """
    Analyze the sentiment of the given text.

    Args:
        text (str): The text to analyze

    Returns:
        dict: A dictionary containing polarity, subjectivity, and assessment
    """
    blob = TextBlob(text)
    sentiment = blob.sentiment
    
    return {
        "polarity": round(sentiment.polarity, 2),  # -1 (negative) to 1 (positive)
        "subjectivity": round(sentiment.subjectivity, 2),  # 0 (objective) to 1 (subjective)
        "assessment": "positive" if sentiment.polarity > 0 else "negative" if sentiment.polarity < 0 else "neutral"
    }

@mcp.tool()
def prime_factors(n: int) -> list[int]:
    """
    Find all prime factors of input integer n

    Args:
        n (int): The integer to find all prime factors for

    Returns:
        list[int]: list of all integer prime factors of n
    """
    factors = []                                                                                                                                                                                     
    d = 2                                                                                                                                                                                            
    while d * d <= n:                                                                                                                                                                                
        while n % d == 0:                                                                                                                                                                            
            factors.append(d)                                                                                                                                                                        
            n //= d                                                                                                                                                                                  
        d += 1                                                                                                                                                                                       
    if n > 1:                                                                                                                                                                                        
        factors.append(n)                                                                                                                                                                            
    return factors   

@mcp.resource("resource://greeting")
def greeting() -> str:
    """Provide weather data as a resource."""
    return "hello world"

@mcp.resource("weather://{location}")
def weather_resource(location: str) -> str:
    """Provide weather data as a resource."""
    return f"Weather data for {location}: Sunny, 72°F"


@mcp.prompt()
def weather_report(location: str) -> str:
    """Create a weather report prompt."""
    return f"""You are a weather reporter. Weather report for {location}?"""


# Run the server
if __name__ == "__main__":
    mcp.run()
