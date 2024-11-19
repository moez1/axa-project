import React from 'react';
import { Container, Typography } from '@mui/material';
import PassengerTable from './components/PassengerTable';

const App = () => {
  return (
    <Container>
      <Typography variant="h3" gutterBottom>
        Titanic Passengers
      </Typography>
      <PassengerTable />
    </Container>
  );
};

export default App;