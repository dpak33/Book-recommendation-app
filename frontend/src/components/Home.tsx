import React from 'react';
import { Link } from 'react-router-dom';

const Home: React.FC = () => {
    return (
        <div>
            <h1>Welcome to Book Recommendation App</h1>
            <Link to="/books">View Books</Link>
        </div>
    );
};

export default Home;