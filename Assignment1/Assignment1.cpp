#include <bits/stdc++.h>
using namespace std;

// Function to load stop words from a file into a set
unordered_set<string> loadStopWords(const string& stopwords_file) {
    unordered_set<string> stopwords;
    ifstream file(stopwords_file);
    string word;
    while (file >> word) {
        stopwords.insert(word);
    }
    return stopwords;
}

// Function to check if a character is punctuation
bool isPunctuation(char c) {
    return ispunct(static_cast<unsigned char>(c));
}

// Basic stemming function (removes 'ing', 'ed', 's')
string stemWord(const string& word) {
    string stemmed_word = word;
    if (word.length() > 4 && word.substr(word.length() - 3) == "ing") {
        stemmed_word = word.substr(0, word.length() - 3);
    } else if (word.length() > 3 && word.substr(word.length() - 2) == "ed") {
        stemmed_word = word.substr(0, word.length() - 2);
    } else if (word.length() > 1 && word.back() == 's') {
        stemmed_word = word.substr(0, word.length() - 1);
    }
    return stemmed_word;
}

// Function to preprocess document: remove punctuation, stopwords, and apply stemming
vector<string> preprocessDocument(const string& doc, const unordered_set<string>& stopwords) {
    istringstream iss(doc);
    string word;
    vector<string> processed_words;
    
    while (iss >> word) {
        // Remove punctuation
        word.erase(remove_if(word.begin(), word.end(), isPunctuation), word.end());
        
        // Convert to lowercase
        transform(word.begin(), word.end(), word.begin(), ::tolower);
        
        // Skip stop words
        if (stopwords.find(word) != stopwords.end()) {
            continue;
        }
        
        // Apply stemming
        string stemmed_word = stemWord(word);
        
        // Add the processed word
        processed_words.push_back(stemmed_word);
    }
    return processed_words;
}

unordered_map<string, int> countWordFrequency(const vector<string>& words) {
    unordered_map<string, int> word_freq;
    for (const auto& word : words) {
        word_freq[word]++;
    }
    return word_freq;
}

void outputWordFrequencies(const unordered_map<string, int>& word_freq, const string& output_file) {
    ofstream out(output_file);
    for (const auto& entry : word_freq) {
        out << entry.first << " : " << entry.second << endl;
    }
}

int main() {
    string stopwords_file = "stopwords.txt";
    string document_file = "document.txt";
    string output_file = "output.txt";
    
    unordered_set<string> stopwords = loadStopWords(stopwords_file);
    
    // Read document content
    ifstream doc_file(document_file);
    stringstream buffer;
    buffer << doc_file.rdbuf();
    string document = buffer.str();
    

    vector<string> processed_words = preprocessDocument(document, stopwords);
    
    // Count word frequency
    unordered_map<string, int> word_freq = countWordFrequency(processed_words);
    
    outputWordFrequencies(word_freq, output_file);
    
    cout << "Document processing completed. Check '" << output_file << "' for results." << endl;
    
    return 0;
}
