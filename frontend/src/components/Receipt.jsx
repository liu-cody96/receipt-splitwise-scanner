import * as React from 'react';
import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableCell from '@mui/material/TableCell';
import TableContainer from '@mui/material/TableContainer';
import TableHead from '@mui/material/TableHead';
import TableRow from '@mui/material/TableRow';
import Paper from '@mui/material/Paper';
import {TagUserInput} from './TagUserInput';
import { useState } from 'react'

const rows = [
  {
    desc:'Paperclips1 (Boasdfx)', 
    price: 1.15,

  },
  {
    desc:'Paperclips2 (Boasdfx)', 
    price: 1.15,

  },
  {
    desc:'Paperclips3 (Basdfox)', 
    price: 1.15,

  },
];

export const ReceiptData = (props) => {
    const [uniqueUsers, setUniqueUsers] = useState();

  return (
    <>

    <div style={{marginBottom: '25px', marginLeft: '250px', marginRight: '250px', marginTop: '25px'}}>
        <h2> Your receipt from {props.data["merchant_name"] }: </h2>
        <TableContainer component={Paper}>
        <Table sx={{  }} aria-label="spanning table">
            <TableHead>
            <TableRow>
                <TableCell align="left">Details</TableCell>
                <TableCell align="left">Price</TableCell>
                <TableCell align="left" colSpan={2}>Add Users</TableCell>
            </TableRow>
            </TableHead>
            <TableBody>
            {rows.map((row) => (
                <TableRow key={row.desc}>
                <TableCell>{row.desc}</TableCell>
                <TableCell align="left">{row.price}</TableCell>
                <TableCell><TagUserInput setUniqueUsers = {setUniqueUsers}></TagUserInput></TableCell>
                </TableRow>
            ))}
            <TableRow>
                <TableCell colSpan={1}>Tip</TableCell>
                <TableCell align="left">{3.44}</TableCell>
                <TableCell><TagUserInput/></TableCell>
            </TableRow>
            <TableRow>
                <TableCell colSpan={1}>Tax</TableCell>
                <TableCell align="left">{3.44}</TableCell>
                <TableCell><TagUserInput/></TableCell>
            </TableRow>
            <TableRow>
                <TableCell colSpan={1}>Total</TableCell>
                <TableCell align="left">{3.44}</TableCell>
                <TableCell></TableCell>
            </TableRow>
            </TableBody>
        </Table>
        </TableContainer>
    </div>
    </>
  );
}

export default ReceiptData;