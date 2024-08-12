import React, { useState, useEffect } from 'react';
import axios from 'axios';

function Visualization() {
  const [visualization, setVisualization] = useState(null);

  useEffect(() => {
    const fetchVisualization = async () => {
      try {
        const response = await axios.get('http://localhost:5000/visualize');
        setVisualization(`data:image/png;base64,${response.data.visualization}`);
      } catch (error) {
        console.error('Error fetching visualization', error);
      }
    };

    fetchVisualization();
  }, []);

  return (
    <div>
      <h2>Visualization</h2>
      {visualization ? (
        <img src={visualization} alt="Data Visualization" />
      ) : (
        <p>Loading visualization...</p>
      )}
    </div>
  );
}

export default Visualization;
