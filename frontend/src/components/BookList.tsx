import React, { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';
import axios from 'axios';

const BookList: React.FC = () => {
    const [books, setBooks] = useState([]);

    useEffect(() => {
        axios.get('/api/books')
            .then(response => setBooks(response.data))
            .catch(error => console.error(error));
    }, []);

    return (
        <div>
            <h1>Book List</h1>
            <ul>
                {books.map((book: any) => (
                    <li key={book.id}>
                        <Link to={`/books/${book.id}`}>{book.title}</Link>
                    </li>
                ))}
            </ul>
        </div>
    );
};

export default BookList;