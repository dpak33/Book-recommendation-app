import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import axios from 'axios';

const BookDetail: React.FC = () => {
    const { id } = useParams<{ id: string }>();
    const [book, setBook] = useState<any>(null);

    useEffect(() => {
        axios.get(`/api/books/${id}`)
            .then(response => setBook(response.data))
            .catch(error => console.error(error));
    }, [id]);

    if (!book) return <div>Loading...</div>;

    return (
        <div>
            <h1>{book.title}</h1>
            <p>{book.description}</p>
        </div>
    );
};

export default BookDetail;