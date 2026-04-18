from transformers import pipeline

def summarize_text(text):
    print("Loading summarization model...")
    # Using a pre-trained summarization pipeline (Default is sshleifer/distilbart-cnn-12-6)
    summarizer = pipeline("summarization")
    
    print("Generating summary...")
    # Generate summary. Max length and min length can be adjusted.
    summary = summarizer(text, max_length=130, min_length=30, do_sample=False)
    
    return summary[0]['summary_text']

if __name__ == "__main__":
    sample_text = (
        "Artificial intelligence (AI) is intelligence demonstrated by machines, as opposed to intelligence displayed by animals and humans. "
        "Leading AI textbooks define the field as the study of 'intelligent agents': any system that perceives its environment and takes actions "
        "that maximize its chance of achieving its goals. Some popular accounts use the term 'artificial intelligence' to describe machines that "
        "mimic 'cognitive' functions that humans associate with the human mind, such as 'learning' and 'problem solving', however, this definition "
        "is rejected by major AI researchers. AI applications include advanced web search engines (e.g., Google Search), recommendation systems "
        "(used by YouTube, Amazon, and Netflix), understanding human speech (such as Siri and Alexa), self-driving cars (e.g., Waymo), generative "
        "or creative tools (ChatGPT and AI art), and competing at the highest level in strategic game systems (such as chess and Go)."
    )
    
    print("Original Text Length:", len(sample_text))
    print("\nOriginal Text:\n", sample_text)
    
    summary = summarize_text(sample_text)
    
    print("\n---\n")
    print("Summary Length:", len(summary))
    print("Summary Text:\n", summary)
