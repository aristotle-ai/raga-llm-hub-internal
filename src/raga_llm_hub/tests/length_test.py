def length_test(response, threshold):
    """
    The number of words in the generated response.
    Args:
        response (str): response generated by your model.
        Pass below instruction to your LLM and ask it to generate output. Refer below example.
        instruction: "# Instruction\n\nGiven several concepts (i.e., nouns or verbs), write a short and simple sentence that contains *all* the required words.\nThe sentence should describe a common scene in daily life, and the concepts should be used in a natural way.\n\n# Examples\n\n## Example 1\n- Concepts: \"dog(noun), frisbee(noun), catch(verb), throw(verb)\"\n- Sentence: The dog catches the frisbee when the boy throws it into the air.\n\n## Example 2\n- Concepts: \"apple(noun), place(verb), tree(noun), pick(verb)\"\n- Sentence: A girl picks some apples from a tree and places them into her basket.\n\n# Your Task \n\n- Concepts: \"catch(verb), dog(noun), frisbee(noun), throw(verb)\"\n- Sentence: ",
        example_response: [
        "The dog catches the frisbee when someone throws it."
        ]
    Returns:
        dict: A dictionary containing the evaluation results.
    """

    length = len(response.split(" "))

    # Prepare and return the result
    result = {"response": response, "score": length, "is_passed": length <= threshold}

    return result
