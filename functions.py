from lexicon import lexicon
import openai, logging

client = openai.OpenAI(api_key='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')

async def generate_fairy_tale(language, child_sex, child_name, child_age, favorite_characters, theme, genre):
    try:
        prompt = lexicon["prompt"].format(genre, language, theme, child_name, child_sex, child_age)
        prompt += f"The favorite characters are {favorite_characters}."
        if favorite_characters == "":
            prompt = lexicon["prompt"].format(genre, language, theme, child_name, child_sex, child_age)
        # prompt += "The story should have a beginning, middle, climax, and end with a consistent storyline."

        response = client.chat.completions.create(
          model="gpt-3.5-turbo",
          messages=[
                {"role": "user", "content": prompt}
            ]
        )

        return response.choices[0].message.content
    except Exception as e:
        logging.error(e)