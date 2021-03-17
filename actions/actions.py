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
            dispatcher.utter_message(text = "credit cards come in 2 variants basic and platinum basic has a limit of 50k rs and platinum 4L rs ")
        elif "loan" in product:
             dispatcher.utter_message(text = "personal loans come in various tiers each having their own rate of interests ranging from 8% to 15 % based on the analysis done by the loan expert")
        elif "insuarance" in product:
             dispatcher.utter_message(text = "abc bank provides 2 kinds of life insuarance, term and endowment. you can know more about them on our solutions page")
        else:
            dispatcher.utter_message(text = "you can know more about {product} on our solutions page ")
        return []
