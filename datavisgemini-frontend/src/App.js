import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import FileUpload from './components/FileUpload';
import Visualization from './components/Visualization';
import Feedback from './components/Feedback';

function App() {
  return (
    <Router>
      <div className="App">
        <Routes>
          <Route path="/upload" element={<FileUpload />} />
          <Route path="/visualization" element={<Visualization />} />
          <Route path="/feedback" element={<Feedback />} />
          <Route path="/" element={<FileUpload />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;