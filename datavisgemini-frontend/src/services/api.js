import axios from 'axios';

const GEMINI_API_URL = 'https://gemini-api-url.com';

export const getFeedback = async () => {
  try {
    const response = await axios.get(`${GEMINI_API_URL}/feedback`, {
      headers: {
        'Authorization': `Bearer ${process.env.REACT_APP_GEMINI_API_KEY}`,
      },
    });
    return response.data;
  } catch (error) {
    console.error('Error fetching feedback from Gemini API', error);
    throw error;
  }
};
