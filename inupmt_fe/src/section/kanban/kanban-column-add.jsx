import { useState, useCallback } from "react"
// @mui
import Paper from "@mui/material/Paper"
import Button from "@mui/material/Button"
import TextField from "@mui/material/TextField"
import { inputBaseClasses } from "@mui/material/InputBase"
import ClickAwayListener from "@mui/material/ClickAwayListener"
// hooks
import { useBoolean } from "./utils/use-boolean"
// utils
import uuidv4 from "./utils/uuidv4"
// api
import { createColumn } from "../../services/kanban"
// components
import Iconify from "./components/iconify"

// ----------------------------------------------------------------------

export default function KanbanColumnAdd() {
  const [columnName, setColumnName] = useState("")

  const openAddColumn = useBoolean()

  const handleChangeName = useCallback(event => {
    setColumnName(event.target.value)
  }, [])

  const handleCreateColumn = useCallback(async () => {
    try {
      if (columnName) {
        createColumn({
          id: uuidv4(),
          name: columnName,
          taskIds: []
        })
        setColumnName("")
      }
      openAddColumn.onFalse()
    } catch (error) {
      console.error(error)
    }
  }, [columnName, openAddColumn])

  const handleKeyUpCreateColumn = useCallback(
    event => {
      if (event.key === "Enter") {
        handleCreateColumn()
      }
    },
    [handleCreateColumn]
  )

  return (
    <Paper sx={{ minWidth: 280, width: 280 }}>
      {openAddColumn.value ? (
        <ClickAwayListener onClickAway={handleCreateColumn}>
          <TextField
            autoFocus
            fullWidth
            placeholder="New section"
            value={columnName}
            onChange={handleChangeName}
            onKeyUp={handleKeyUpCreateColumn}
            sx={{
              [`& .${inputBaseClasses.input}`]: {
                typography: "h6"
              }
            }}
          />
        </ClickAwayListener>
      ) : (
        <Button
          fullWidth
          size="large"
          color="inherit"
          variant="outlined"
          startIcon={<Iconify icon="mingcute:add-line" sx={{ mr: -0.5 }} />}
          onClick={openAddColumn.onTrue}
        >
          Add Section
        </Button>
      )}
    </Paper>
  )
}
