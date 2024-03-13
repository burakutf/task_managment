// @mui
import Paper from "@mui/material/Paper"
import Stack from "@mui/material/Stack"
import Button from "@mui/material/Button"
import Avatar from "@mui/material/Avatar"
import InputBase from "@mui/material/InputBase"
import IconButton from "@mui/material/IconButton"
// hooks
import { useMockedUser } from "./utils/use-mocked-user"
// components
import Iconify from "./components/iconify"

// ----------------------------------------------------------------------
import React, { useState } from 'react';
import { addComment } from "../../services/kanban"
// ...other imports...

export default function KanbanDetailsCommentInput({ task }) {
  const { user } = useMockedUser();
  const [comment, setComment] = useState(''); // Add this line

  const handleCommentSubmit = () => {
    // Add your logic to submit the comment here
    addComment({ task: task.id, content: comment }) // Call the addComment function with the task ID and comment
    setComment(''); // Clear the comment input after submit
  };

  return (
    <Stack
      direction="row"
      spacing={2}
      sx={{
        py: 3,
        px: 2.5
      }}
    >
      <Avatar src={user?.photoURL} alt={user?.displayName} />

      <Paper
        variant="outlined"
        sx={{ p: 1, flexGrow: 1, bgcolor: "transparent" }}
      >
        <InputBase
          fullWidth
          multiline
          rows={2}
          placeholder="Type a message"
          sx={{ px: 1 }}
          value={comment} // Bind the value to the state variable
          onChange={(e) => setComment(e.target.value)} // Update the state variable when the input changes
        />

        <Stack direction="row" alignItems="center">
          <Stack direction="row" flexGrow={1}>
            <IconButton>
              <Iconify icon="solar:gallery-add-bold" />
            </IconButton>

            <IconButton>
              <Iconify icon="eva:attach-2-fill" />
            </IconButton>
          </Stack>

          <Button variant="contained" onClick={handleCommentSubmit}>Comment</Button> {/* Add an onClick handler here */}
        </Stack>
      </Paper>
    </Stack>
  )
}