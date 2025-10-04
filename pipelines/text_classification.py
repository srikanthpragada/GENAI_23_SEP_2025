from transformers import pipeline

classifier = pipeline("zero-shot-classification", model = "facebook/bart-large-mnli" )
output = classifier(
    "Apple released it new version of iPhone - iPhone 17 models",
    candidate_labels = ["education", "politics", "business"],
)
print(output)