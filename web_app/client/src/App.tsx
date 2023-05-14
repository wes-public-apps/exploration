import React from 'react';
import { BrowserRouter, Routes, Route, useLocation } from "react-router-dom";
import { ApolloProvider, ApolloClient, InMemoryCache } from '@apollo/client';

import './App.css';
import AboutPage from './pages/about';
import ErrorPage from './pages/error_page';
import Form from './pages/new_mission';
import HomePage from './pages/home';
import logo from './logo.svg';

const client = new ApolloClient({
  uri: "https://" + window.location.host + "/mission_manager",
  cache: new InMemoryCache(),
});

function App() {
  return (
    <div className="App">
      <BrowserRouter>
        <Routes>
				  <Route path='about' element={<AboutPage />} />
				  <Route path='new-mission' element={<ApolloProvider client={client}><Form /></ApolloProvider>} />
				  <Route path='/' element={<HomePage />} />
				  <Route path='*' element={<ErrorPage />} />
        </Routes>
      </BrowserRouter>
    </div>
  );
}

export default App;
