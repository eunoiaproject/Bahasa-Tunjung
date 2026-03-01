const fs = require('fs');
const path = './translations.json';

/**
 * Load data from the JSON file
 */
const loadData = () => {
    try {
        const dataBuffer = fs.readFileSync(path);
        return JSON.parse(dataBuffer.toString());
    } catch (e) {
        return { tonyooi_to_id: {} };
    }
};

/**
 * Save data to the JSON file
 */
const saveData = (data) => {
    fs.writeFileSync(path, JSON.stringify(data, null, 2));
};

/**
 * Add or Update a word
 * @param {string} tonyooi - The source word
 * @param {string} indonesia - The translation
 */
const upsertWord = (tonyooi, indonesia) => {
    const data = loadData();
    const wordKey = tonyooi.toLowerCase();
    
    const isUpdate = data.tonyooi_to_id[wordKey] !== undefined;
    data.tonyooi_to_id[wordKey] = indonesia.toLowerCase();
    
    saveData(data);
    console.log(isUpdate ? `✅ Updated: ${tonyooi}` : `➕ Added: ${tonyooi}`);
};

/**
 * Translate a word
 */
const translate = (word) => {
    const data = loadData();
    const result = data.tonyooi_to_id[word.toLowerCase()];
    return result ? result : "❌ Word not found.";
};

// --- Examples of usage ---
// upsertWord('nasi', 'nasi'); // Adds a word
// console.log(translate('nasi')); // Translates
