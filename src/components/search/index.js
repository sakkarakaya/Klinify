import React, { useState } from "react";
import { TextField } from '@material-ui/core';
import Button from '@material-ui/core/Button';
import MenuItem from '@material-ui/core/MenuItem';
import { makeStyles } from '@material-ui/core/styles';


const cities = [
  {
    value: 'Braunschweig',
    label: 'Braunschweig'
  },
  {
    value: 'Hannover',
    label: 'Hannover'
  },
  {
    value: 'Göttingen',
    label: 'Göttingen'
  }
];

const useStyles = makeStyles((theme) => ({
  root: {
    '& .MuiTextField-root': {
      margin: theme.spacing(1),
      width: '25ch',
    },
  },
  buttons: {
    width: '200px',
    height: '57px',
    marginRight : '10px'
  },
  searchbutton: {
    width: '200px',
    height: '57px',
    marginRight : '10px',
    backgroundColor: 'lightgreen',
    '&:hover': {
      backgroundColor: 'green',
      borderColor: '#0062cc',
      boxShadow: 'none',
    },
  }
}));

  const Search = (props) => {
  
  const classes = useStyles();
  const [city, setCity] = React.useState();

  const handleChange = (event) => {
    setCity(event.target.value);
  };

  const [searchText, setSearchText] = useState("");
  console.log(searchText);
  return (
    <div>
      <TextField className={classes.buttons} id="outlined-basic" label="Clinic name" variant="outlined" onChange={(event) => setSearchText(event.target.value)} />

      <TextField
        id="outlined-select-currency"
        select
        label="Select city"
        value={city}
        onChange={handleChange}
        variant="outlined"
        className={classes.buttons}
      >
        {cities.map((option) => (
          <MenuItem key={option.value} value={option.value}>
            {option.label}
          </MenuItem>
        ))}
      </TextField>

      <Button className={classes.searchbutton} variant="outlined" color="green" type="submit" id="btn-suche" onClick={() => props.searchedText(searchText)}>Search</Button>

      <button className={classes.buttons} type="submit" id="btn-sort">Sort</button>
    </div>

  );

};

export default Search;
