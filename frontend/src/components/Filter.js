import React from 'react';

const Filter = ({ onFilter }) => {
  const handleFilterChange = (e) => {
    onFilter(e.target.value);
  };

  return (
    <input type="text" placeholder="Filter by name" onChange={handleFilterChange} />
  );
};

export default Filter;