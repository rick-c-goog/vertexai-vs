import vertexai
from vertexai.preview.language_models import TextGenerationModel
from google.cloud import aiplatform

def predict_llm_property( input_text: str):
    
    vertexai.init(project="rick-vertex-ai", location="us-central1")
    parameters = {
      "temperature": 0.8,
      "max_output_tokens": 512,
      "top_p": 0.8,
      "top_k": 35
    }

    model = TextGenerationModel.from_pretrained("text-bison@001")
    print("debug rick")
    response = model.predict(
    """You are real estate agent, you need to re-write and publish property listing that is attractive to potential buyers with following requirements:
based on key facts from information provided
Tells a Story
Highlight the unobvious
Use keywords
Sell benefits, not features
Narrate the journey through the home
Include a call to action
Do not overshare
Get specific
Keep it short and succinct
Include that one, most marketable feature
Use descriptive words that compel the buyer to learn more
Include a benefit relative to the location
Write several headlines, read them out loud and pick the best one
Craft a great headline
Tell a compelling story
Emphasize the location
Focus on key facts and features
Do not forget a call to action
Keep it short
Accentuate the key amenities
Less than 400 words

Examples:
A REWARDING ESCAPE PEACEFULLY SITUATED: Luxurious and upgraded, this 4 bedroom, 4.5 bathroom home of 5,281 sq. ft. (including poolhouse, per independent third-party measurement) rests on a lot of 1.23 acres (per county) on a peaceful cul-de-sac in the Lakeside neighborhood. Richly-appointed spaces include large gathering areas, a bright, professional-grade kitchen, spectacular dining room, two walk-out master suites, and a home theater. Contemporary amenities include solar PV and a Tesla EV charging station. The expansive backyard includes a sparkling pool and spa plus a comfortable poolhouse all in private, verdant surroundings. You will appreciate the short drive to downtown Los Altos, Rancho Shopping Center, access to Interstate 280, and numerous parks and preserves.

Stunning large late 80s contemporary home with soaring ceilings and windows, split levels, great floor plan including open dining and living room. Located in the beautiful hilly and treed, desirable Windmill Hill section of Desoto you are conveniently located to shops, dining, and 20 minutes to downtown Dallas. This 3 bedroom, 3.1 bath home is large and accommodating to both guests for entertaining with 2 living areas, office, wet bar, with a Master suite located on the 1st floor. Great structure and bones and are waiting for new owners to bring their decorating ideas. Wonderful opportunity!

input: {input_text} 


""".format(input_text=input_text),
    **parameters
)
    print(response.text)
    return response.text 