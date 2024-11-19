import React, { useState, useEffect } from 'react';
import axios from 'axios';
import {
  Table, TableBody, TableCell, TableContainer, TableHead, TableRow, Paper,
  Button, TextField, Dialog, DialogActions, DialogContent, DialogTitle, Typography
} from '@mui/material';

const PassengerTable = () => {
  const [passengers, setPassengers] = useState([]);
  const [editingPassenger, setEditingPassenger] = useState(null);
  const [newPassenger, setNewPassenger] = useState({ name: '', sex: '', age: '' });
  const [filter, setFilter] = useState('');
  const [open, setOpen] = useState(false);

  useEffect(() => {
    fetchPassengers();
  }, []);

  const fetchPassengers = () => {
    axios.get('http://localhost:5000/passengers/')
      .then(response => {
        setPassengers(response.data);
      })
      .catch(error => {
        console.error("There was an error fetching the passengers!", error);
      });
  };

  const handleDelete = (id) => {
    axios.delete(`http://localhost:5000/passengers/${id}/`)
      .then(() => {
        fetchPassengers();
      })
      .catch(error => {
        console.error("There was an error deleting the passenger!", error);
      });
  };

  const handleEdit = (passenger) => {
    setEditingPassenger(passenger);
    setOpen(true);
  };

  const handleUpdate = () => {
    axios.put(`http://localhost:5000/passengers/${editingPassenger.id}/`, editingPassenger)
      .then(() => {
        setEditingPassenger(null);
        setOpen(false);
        fetchPassengers();
      })
      .catch(error => {
        console.error("There was an error updating the passenger!", error);
      });
  };

  const handleCreate = () => {
    axios.post('http://localhost:5000/passengers/', newPassenger)
      .then(() => {
        setNewPassenger({ name: '', sex: '', age: '' });
        fetchPassengers();
      })
      .catch(error => {
        console.error("There was an error creating the passenger!", error);
      });
  };

  const handleClose = () => {
    setOpen(false);
    setEditingPassenger(null);
  };

  const handleFilterChange = (event) => {
    setFilter(event.target.value);
  };

  const filteredPassengers = passengers.filter(passenger =>
    passenger.name.toLowerCase().includes(filter.toLowerCase())
  );

  return (
    <div>
      <Typography variant="h5" gutterBottom>
        Create New Passenger
      </Typography>
      <TextField
        label="Name"
        value={newPassenger.name}
        onChange={(e) => setNewPassenger({ ...newPassenger, name: e.target.value })}
        margin="normal"
      />
      <TextField
        label="Sex"
        value={newPassenger.sex}
        onChange={(e) => setNewPassenger({ ...newPassenger, sex: e.target.value })}
        margin="normal"
      />
      <TextField
        label="Age"
        type="number"
        value={newPassenger.age}
        onChange={(e) => setNewPassenger({ ...newPassenger, age: e.target.value })}
        margin="normal"
      />
      <Button variant="contained" color="primary" onClick={handleCreate} style={{ marginTop: '16px' }}>
        Create
      </Button>

      <Typography variant="h5" gutterBottom style={{ marginTop: '32px' }}>
        Passengers
      </Typography>
      <TextField
        label="Filter by Name"
        value={filter}
        onChange={handleFilterChange}
        margin="normal"
        fullWidth
      />
      <TableContainer component={Paper}>
        <Table>
          <TableHead>
            <TableRow>
              <TableCell>Name</TableCell>
              <TableCell>Sex</TableCell>
              <TableCell>Age</TableCell>
              <TableCell>Actions</TableCell>
            </TableRow>
          </TableHead>
          <TableBody>
            {filteredPassengers.map(passenger => (
              <TableRow key={passenger.id}>
                <TableCell>{passenger.name}</TableCell>
                <TableCell>{passenger.sex}</TableCell>
                <TableCell>{passenger.age}</TableCell>
                <TableCell>
                  <Button variant="contained" color="primary" onClick={() => handleEdit(passenger)}>
                    Edit
                  </Button>
                  <Button variant="contained" color="secondary" onClick={() => handleDelete(passenger.id)} style={{ marginLeft: '8px' }}>
                    Delete
                  </Button>
                </TableCell>
              </TableRow>
            ))}
          </TableBody>
        </Table>
      </TableContainer>

      <Dialog open={open} onClose={handleClose}>
        <DialogTitle>Edit Passenger</DialogTitle>
        <DialogContent>
          <TextField
            label="Name"
            value={editingPassenger?.name || ''}
            onChange={(e) => setEditingPassenger({ ...editingPassenger, name: e.target.value })}
            margin="normal"
            fullWidth
          />
          <TextField
            label="Sex"
            value={editingPassenger?.sex || ''}
            onChange={(e) => setEditingPassenger({ ...editingPassenger, sex: e.target.value })}
            margin="normal"
            fullWidth
          />
          <TextField
            label="Age"
            type="number"
            value={editingPassenger?.age || ''}
            onChange={(e) => setEditingPassenger({ ...editingPassenger, age: e.target.value })}
            margin="normal"
            fullWidth
          />
        </DialogContent>
        <DialogActions>
          <Button onClick={handleClose} color="primary">
            Cancel
          </Button>
          <Button onClick={handleUpdate} color="primary">
            Update
          </Button>
        </DialogActions>
      </Dialog>
    </div>
  );
};

export default PassengerTable;