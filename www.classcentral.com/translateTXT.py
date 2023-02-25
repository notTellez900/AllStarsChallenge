import os
import re
import codecs
import subprocess

# Path to the OpenNMT installation directory
OPENNMT_DIR = "C:/Python311/Lib/site-packages/OpenNMT_py-3.0.4.dist-info"

# Path to the source and target language models
SRC_MODEL = "model/iwslt_en_vi_step_1000.pt"
TGT_MODEL = "model/iwslt_vi_en_step_1000.pt"

# Regular expression pattern to match text without HTML tags
PATTERN = r"(?<=^|>)[^><]+?(?=<|$)"

# Function to translate a sentence using OpenNMT
def translate_sentence(sentence, src_lang="en", tgt_lang="vi"):
    # Build the OpenNMT command
    cmd = [
        "onmt_translate",
        "-model", TGT_MODEL if src_lang == "vi" else SRC_MODEL,
        "-src", "-",
        "-tgt", "-",
        "-replace_unk",
        "-beam_size", "5",
        "-batch_size", "1",
        "-n_best", "1",
        "-max_length", "50",
        "-min_length", "5",
        "-quiet",
    ]
    # Run the OpenNMT command
    proc = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    # Write the sentence to the input stream
    proc.stdin.write(sentence.encode("utf-8"))
    proc.stdin.close()
    # Read the translated sentence from the output stream
    translated_sentence = proc.stdout.read().decode("utf-8").strip()
    # Check for errors
    stderr = proc.stderr.read().decode("utf-8").strip()
    if stderr:
        raise Exception(stderr)
    # Return the translated sentence
    return translated_sentence

# Function to translate a file using OpenNMT
def translate_file(input_file, output_file, src_lang="en", tgt_lang="vi"):
    # Read the input file
    with codecs.open(input_file, "r", "utf-8") as f:
        text = f.read()
    # Find all text without HTML tags
    matches = re.findall(PATTERN, text, re.MULTILINE | re.DOTALL)
    # Translate each sentence
    translations = []
    for sentence in matches:
        translation = translate_sentence(sentence, src_lang=src_lang, tgt_lang=tgt_lang)
        translations.append(translation)
    # Replace the original text with the translated text
    for i, sentence in enumerate(matches):
        text = text.replace(sentence, translations[i])
    # Write the output file
    with codecs.open(output_file, "w", "utf-8") as f:
        f.write(text)

# Example usage
input_file = "input.html"
output_file = "output.html"
translate_file(input_file, output_file, src_lang="en", tgt_lang="vi")
