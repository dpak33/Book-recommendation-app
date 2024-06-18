import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Home from './components/Home';
import BookList from './components/BookList';
import BookDetail from './components/BookDetail';

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/books" element={<BookList />} />
        <Route path="/books/:id" element={<BookDetail />} />
      </Routes>
    </Router>
  );
}

export default App;
