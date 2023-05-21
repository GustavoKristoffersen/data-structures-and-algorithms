class Node {
    constructor() {
        this.children = {};   
    }
}


class Trie {
    constructor() {
        this.root = new Node();
    }

    // O(K)
    insert(word) {
        let currentNode = this.root;
        for (let char of word) {
            if (currentNode.children[char]) {
                currentNode = currentNode.children[char];
            }
            else {
                let newNode = new Node();
                currentNode.children[char] = newNode;
                currentNode = newNode;
            }
        }
        currentNode.children['*'] = null;
        return this;
    }

    
    // O(K)
    search(word) {
        let currentNode = this.root;
        for (let char of word) {
            if (currentNode.children[char]) {
                currentNode = currentNode.children[char];
            }
            else {
                return null;
            }
        }
        return currentNode;
    }
    
    autoComplete(word) {
        let currentNode = this.search(word);
        if (!currentNode) {
            return [];
        }
        return this._collectAllWords(currentNode);
    }


    _collectAllWords(node=null, word='', words=[]) {
        let currentNode = node || this.root;
        for (let key of Object.keys(currentNode.children)) {
            let childNode = currentNode.children[key];
            if (key === '*') {
                words.push(word);
            }
            else {
                this._collectAllWords(childNode, word + key, words);
            }
        }
        return words;
    }

    autoCorrect(word) {
        let wordFound = '';
        let currentNode = this.root;
        for (let char of word) {
            if(currentNode.children[char]) {
                wordFound = wordFound + char;
                currentNode = currentNode.children[char];
            }
            else {
                let possibleWords = this._collectAllWords(currentNode);
                if(possibleWords.length > 0) {
                    return wordFound + possibleWords[0]
                } 
                return possibleWords;
            }
        }
        return word;
    }
}
