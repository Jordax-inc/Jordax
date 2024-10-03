from fastapi import FastAPI


def initialize_app():
    # Other app setup code here
    return FastAPI()


app = initialize_app()
