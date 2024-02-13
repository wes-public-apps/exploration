import React, { useState } from 'react';
import { useMutation } from '@apollo/client';
import { ADD_ITEM, AddItemVariables } from './mutations';
import styles from './NewMission.module.css';

const Form: React.FC = () => {
  const [id, setId] = useState('');
  const [name, setName] = useState('');
  const [files, setFiles] = useState<File[]>([]);
  const [successMessage, setSuccessMessage] = useState('');

  const [addItem, { loading }] = useMutation(ADD_ITEM);

  const handleIdChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    setId(event.target.value);
  };

  const handleNameChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    setName(event.target.value);
  };

  const handleFilesChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    if (event.target.files) {
      setFiles(Array.from(event.target.files));
    }
  };

  const handleSubmit = async (event: React.FormEvent<HTMLFormElement>) => {
    event.preventDefault();

    const variables: AddItemVariables = {
      id,
      name,
      files,
    };

    try {
      await addItem({ variables });
      setSuccessMessage('Item added successfully!');
      setId('');
      setName('');
      setFiles([]);
    } catch (error) {
      console.error(error);
    }
  };

  return (
    <div className={styles.container}>
      <form onSubmit={handleSubmit}>
        <div className={styles.inputGroup}>
          <label htmlFor="id">ID:</label>
          <input type="text" id="id" value={id} onChange={handleIdChange} required />
        </div>

        <div className={styles.inputGroup}>
          <label htmlFor="name">Name:</label>
          <input type="text" id="name" value={name} onChange={handleNameChange} required />
        </div>

        <div className={styles.inputGroup}>
          <label htmlFor="files">Files:</label>
          <input type="file" id="files" multiple onChange={handleFilesChange} required />
        </div>

        <button type="submit" disabled={loading}>
          {loading ? 'Submitting...' : 'Submit'}
        </button>
      </form>

      {successMessage && <p className={styles.successMessage}>{successMessage}</p>}
    </div>
  );
};

export default Form;
