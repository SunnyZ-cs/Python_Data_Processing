#!/usr/bin/env python3

Project Infinite Story


import os
import sys
import json
from venv import create

from notopenai import NotOpenAI
from graphics import Canvas

# go to notopenai.com and get your free api key
CLIENT = NotOpenAI(api_key="c9074dd9-b72d-452b-9b17-db42f3c9237e")
CANVAS_WIDTH = 600
CANVAS_HEIGHT = 600


def is_unknown_scene(story, scene_key):
    Return True if this scene_key is not present in the story scenes,
    i.e. it is an unknown scene.
    >>> story = {'plot': 'xyz', 'scenes': {'start': {}, 'go_outside': {}}}
    >>> is_unknown_scene(story, 'go_outside')
    False
    >>> is_unknown_scene(story, 'selfie_with_celeb')
    True
    if scene_key in story['scenes']:
        return False
    return True


def unknown_scenes(story):
    Look at all the scenes, and within them,
    all the choices. Return a list of all the scene_key
    strings which are unknown.
    >>> story = json.load(open('data/tiny.json'))
    >>> unknown_scenes(story)
    ['scene_bbb', 'scene_ccc']
    >>> story = json.load(open('data/original_small.json'))
    >>> unknown_scenes(story)
    ['next_to_gully', 'descend_into_valley', 'watching_sunset', 'continue_exploring_hilltop', 'return_to_small_brick_building']
    unknown_list = []
    all_scenes = story['scenes']
    for scene in all_scenes.keys():
        scene_data = all_scenes[scene]
        scene_choices = scene_data['choices']
        for choices_data in scene_choices:
            scene_key_str = choices_data['scene_key']
            if is_unknown_scene(story, scene_key_str):
                unknown_list.append(scene_key_str)
    return unknown_list





def create_new_scene(story, scene_key):
    Given story and scene_key, create and return
    a new scene dict for that scene_key using the AI.
    # Your code here
    all_scenes = story['scenes']
    prompt = (f'Return the next scene of a story for key {scene_key}. '
              + f'An example scene should be formatted in json '
              + f'like this: {json.dumps(all_scenes['start'])}. '
              + f'The main plot line of the story is {story['plot']}.')


    # The rest of the code for this function is provided below,
    # sending the prompt to the AI and returning what it returns.
    # (Identical code to the lecture example).
    chat_completion = CLIENT.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        model="gpt-3.5-turbo",
        response_format={"type": "json_object"},
    )
    json_response = chat_completion.choices[0].message.content
    return json.loads(json_response)


def next_scene(story, scene_key):
    Given a story and scene_key. If the scene_key is unknown,
    construct a new scene dict via the AI and insert the new scene
    dict into the story. In all cases, return the scene dict
    from the story for this scene_key.
    all_scenes = story['scenes']
    if is_unknown_scene(story, scene_key):
        new_scene = create_new_scene(story, scene_key)
        all_scenes[scene_key] = new_scene
    return all_scenes[scene_key]




def run_story(filename):
    (provided code)
    Given filename for a story, run the user through
    the story. Begin at the "start" scene, and then let
    the user pick the next scene.
    with open(filename) as f:
        story = json.load(f)

    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT, 'Infinite Story')
    curr_scene_key = 'start'
    while curr_scene_key != 'q':
        scene = next_scene(story, curr_scene_key)

        # Have scene - print it out, prompt for next scene key
        print_scene(story, scene)
        show_illustration(canvas, curr_scene_key)
        curr_scene_key = prompt_next_key(scene)


def print_scene(story, scene):
    (provided code)
    Print out the scene and prints its list of choices.
    print("")
    print(scene['text'])
    
    if 'choices' in scene:
        choices = scene['choices']

        for i in range(len(choices)):
            # choice has 'text' and 'scene_key'
            choice = choices[i]
            next_key = choice['scene_key']
            suffix = ''
            if is_unknown_scene(story, next_key):
                suffix = '*'
            print(f"{i+1}{suffix}. {choice['text']}")
        print('q. quit')


def prompt_next_key(scene):
    (provided code)
    Get the next scene_key the user wants, or q to quit
    choices = scene['choices']

    while True:
        choice = input("What do you choose? ")
        if choice == 'q':
            return choice
        if choice.isdigit():
            i = int(choice) - 1  # index numbers are -1 from user-entry numbers
            if i >= 0 and i < len(choices):
                return choices[i]['scene_key']
        print('Please enter a valid number or q')


def show_illustration(canvas, scene_key):
    "Display an image for this scene_key if available."
    illustration_path = f"img/{scene_key}.jpg"
    if os.path.exists(illustration_path):
        canvas.clear()
        canvas.create_image_with_size(0, 0, CANVAS_WIDTH, CANVAS_HEIGHT, illustration_path)
        canvas.create_rectangle(0, CANVAS_HEIGHT - 32, 200, CANVAS_HEIGHT, color="#ffffff")
    else:
        canvas.clear()
        canvas.create_rectangle(0, 0, CANVAS_WIDTH, CANVAS_HEIGHT, "black")
        canvas.create_rectangle(80, 80,
                                CANVAS_WIDTH - 80,
                                CANVAS_HEIGHT - 80,
                                color = "lightblue")


def main():
    args = sys.argv[1:]

    if len(args) == 1:
        run_story(args[0])
    else:
        print('example usage: data/original_small.json')


if __name__ == "__main__":
    main()

