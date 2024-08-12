import React, { useState, useEffect } from 'react';
import axios from 'axios';

function Feedback() {
  const [feedback, setFeedback] = useState('');

  useEffect(() => {
    const fetchFeedback = async () => {
      try {
        const response = await axios.get('https://gemini-api-url.com/feedback', {
          headers: {
            'Authorization': `Bearer ${process.env.REACT_APP_GEMINI_API_KEY}`
          }
        });
        setFeedback(response.data.feedback);
      } catch (error) {
        console.error('Error fetching feedback', error);
        setFeedback('Error fetching feedback');
      }
    };

    fetchFeedback();
  }, []);

  return (
    <div>
      <h2>Feedback</h2>
      <p>{feedback}</p>
    </div>
  );
}

export default Feedback;