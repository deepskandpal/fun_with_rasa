# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
from rasa_sdk.events import SlotSet
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ExplainProducts(Action):

    def name(self) -> Text:
        return "explain_products"

    def run(self, dispatcher, tracker, domain):
        product = tracker.get_slot('product')
        if "credit" in product:
            dispatcher.utter_message(text = "credit cards are the best")
        elif "loan" in product:
             dispatcher.utter_message(text = "loans are great")
        elif "insuarance" in product:
             dispatcher.utter_message(text = "insuarance is a subject matter to market risk")
        else:
            dispatcher.utter_message(text = "you can know more about {product} on our solutions page ")
        return []
