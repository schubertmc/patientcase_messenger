## anki bot 
import os
from anki.collection import Collection
from bs4 import BeautifulSoup
import html
import html2text


def getCards(collection_path, search_string):
    # Open the Anki collection
    col = Collection(collection_path)


    try: 
        target_cards = {}

        #Access cards
        for cid in col.find_cards(search_string):
            card = col.get_card(cid)
            note = col.get_note(card.nid)
            #print(f"Card ID: {card.id}, Front: {note.fields[0]}, Back: {note.fields[1]}")
            card = {card.id: {"front":note.fields[0], "back":note.fields[1]}}
            target_cards.update(card)

        col.close()
    except Exception as e:
        print(str(e))
        col.close()


    return target_cards


def getCardString(cardx):
    front = cardx["front"]
    back = cardx["back"]
    text = f"Front:\n{clean_html(front)}---\nBack:\n{clean_html(back)}"
    return text


def clean_html(content):

    converter = html2text.HTML2Text()
    converter.ignore_links = False  
    # Convert HTML to Markdown
    markdown_content = converter.handle(content)
    return markdown_content



print("ankiaccess loaded.")
