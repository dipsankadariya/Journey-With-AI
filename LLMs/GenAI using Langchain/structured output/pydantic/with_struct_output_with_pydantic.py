#simple example of structured output with schema
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from typing import Optional,Literal
from pydantic import BaseModel,Field

load_dotenv()
model= ChatGoogleGenerativeAI(
    model="gemini-3.6-flash"
)
#schema
class Review(BaseModel):
    key_themes:list[str]=Field(description="List the key themes of the product review")
    summary:str=Field(description="A brief summary of the review")
    sentiment:Literal["positive", "negative"]=Field(description="Return the sentiment of the review")
    pros:Optional[list[str]]=Field(default=None, description="List the pros of the product")
    cons:Optional[list[str]]=Field(default=None, description="List the cons of the product")
    name:Optional[str]=Field(default=None, description="Name of the product")
structured_mode=model.with_structured_output(Review)

result=structured_mode.invoke("""
The iPhone is a premium smartphone that combines powerful performance, a high-quality display, advanced cameras, and Apple's polished iOS ecosystem. It features a 6.1-inch Super Retina XDR OLED display with excellent brightness, sharp resolution, HDR support, and vibrant colors. The device is powered by a modern Apple A-series chip and comes with 8 GB of RAM, while storage options can range from 128 GB to 512 GB depending on the model. Its camera system includes a 48 MP main camera along with additional lenses for ultra-wide and other photography capabilities, supporting high-quality photos and 4K video recording. Connectivity features include 5G, Wi-Fi, Bluetooth, NFC, Face ID, and USB-C, while wireless and fast charging provide additional convenience. The iPhone runs on iOS, which offers a smooth interface, strong security, long-term software updates, and excellent integration with products such as MacBooks, Apple Watches, and AirPods. The premium glass-and-metal design also provides a solid and sophisticated feel, along with water and dust resistance.

Pros: Excellent performance, high-quality OLED display, impressive camera and video quality, smooth and reliable iOS experience, strong security, long software support, premium build quality, and excellent ecosystem integration.

Cons: High price compared with many Android alternatives, limited customization, storage upgrades can be expensive, and some features may be restricted to Apple's ecosystem""")


print(result.key_themes)
print(result.name)
print(result.summary)
print(result.sentiment)
print(result.pros)
print(result.cons)