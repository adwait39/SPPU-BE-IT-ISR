#include <bits/stdc++.h>
using namespace std;

unordered_map<string, vector<int>> buildInvertedIndex(const string& text) {
    unordered_map<string, vector<int>> invertedIndex;
    istringstream iss(text);
    string word;
    int position = 0;

    while (iss >> word) {
        // Clean the word: remove punctuation and convert to lowercase
        word.erase(remove_if(word.begin(), word.end(), ::ispunct), word.end());
        transform(word.begin(), word.end(), word.begin(), ::tolower);
        
        invertedIndex[word].push_back(position);
        position++;
    }
    return invertedIndex;
}


void printInvertedIndex(const unordered_map<string, vector<int>>& invertedIndex) {
    cout << "Inverted Index:" << endl;
    for (const auto& pair : invertedIndex) {
        cout << pair.first << ": ";
        for (int pos : pair.second) {
            cout << pos << " ";
        }
        cout << endl;
    }
}

// Function to search for a query in the inverted index
void searchQuery(const unordered_map<string, vector<int>>& invertedIndex, const string& query) {
    string cleanedQuery = query;
    cleanedQuery.erase(remove_if(cleanedQuery.begin(), cleanedQuery.end(), ::ispunct), cleanedQuery.end());
    transform(cleanedQuery.begin(), cleanedQuery.end(), cleanedQuery.begin(), ::tolower);

    auto it = invertedIndex.find(cleanedQuery);
    if (it != invertedIndex.end()) {
        cout << "Occurrences of \"" << cleanedQuery << "\": ";
        for (int pos : it->second) {
            cout << pos << " ";
        }
        cout << endl;
    } else {
        cout << "\"" << cleanedQuery << "\" not found in the text." << endl;
    }
}

int main() {

    string text = "This is a text. A text has many words. Words are made from letters.";
    
    // Build the inverted index
    unordered_map<string, vector<int>> invertedIndex = buildInvertedIndex(text);
    
    printInvertedIndex(invertedIndex);

    // Input query from user
    string query;
    cout << "Enter a word to search: ";
    getline(cin, query);
    
    // Search for the query
    searchQuery(invertedIndex, query);

    return 0;
}
