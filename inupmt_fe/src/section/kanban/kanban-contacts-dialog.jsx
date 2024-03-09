import { useState, useCallback } from "react"
// @mui
import Box from "@mui/material/Box"
import Button from "@mui/material/Button"
import Avatar from "@mui/material/Avatar"
import Dialog from "@mui/material/Dialog"
import ListItem from "@mui/material/ListItem"
import TextField from "@mui/material/TextField"
import Typography from "@mui/material/Typography"
import DialogTitle from "@mui/material/DialogTitle"
import ListItemText from "@mui/material/ListItemText"
import DialogContent from "@mui/material/DialogContent"
import InputAdornment from "@mui/material/InputAdornment"
import ListItemAvatar from "@mui/material/ListItemAvatar"
// components
import Iconify from "./components/iconify"
import SearchNotFound from "./components/search-not-found"
import { _contacts } from "./mock/_others";
// ----------------------------------------------------------------------

const ITEM_HEIGHT = 64

export default function KanbanContactsDialog({ assignee = [], open, onClose }) {
  const [searchContact, setSearchContact] = useState("")

  const handleSearchContacts = useCallback(event => {
    setSearchContact(event.target.value)
  }, [])

  const dataFiltered = applyFilter({
    inputData: _contacts,
    query: searchContact
  })

  const notFound = !dataFiltered.length && !!searchContact

  return (
<Dialog fullWidth maxWidth="xs" open={open} onClose={onClose}>
  <DialogTitle sx={{ pb: 0 }}>
    Contacts <Typography component="span">({_contacts.length})</Typography>
  </DialogTitle>

  <Box sx={{ px: 3, py: 2.5 }}>
    <TextField
      fullWidth
      value={searchContact}
      onChange={handleSearchContacts}
      placeholder="Search..."
      InputProps={{
        startAdornment: (
          <InputAdornment position="start">
            <Iconify
              icon="eva:search-fill"
              sx={{ color: "text.disabled" }}
            />
          </InputAdornment>
        )
      }}
    />
  </Box>

  <DialogContent sx={{ p: 0 }}>
    {notFound ? (
      <SearchNotFound query={searchContact} sx={{ mt: 3, mb: 10 }} />
    ) : (
      <Box
        sx={{
          px: 2.5,
          height: ITEM_HEIGHT * 6,
          overflow: 'auto' // Scroll özelliğini aktif hale getiriyoruz
        }}
      >
        {dataFiltered.map(contact => {
          const checked = assignee
            .map(person => person.name)
            .includes(contact.name)

          return (
            <ListItem
              key={contact.id}
              disableGutters
              secondaryAction={
                <Button
                  size="small"
                  color={checked ? "primary" : "inherit"}
                  startIcon={
                    <Iconify
                      width={16}
                      icon={
                        checked ? "eva:checkmark-fill" : "mingcute:add-line"
                      }
                      sx={{ mr: -0.5 }}
                    />
                  }
                >
                  {checked ? "Assigned" : "Assign"}
                </Button>
              }
              sx={{ height: ITEM_HEIGHT }}
            >
              <ListItemAvatar>
                <Avatar src={contact.avatarUrl} />
              </ListItemAvatar>

              <ListItemText
                primaryTypographyProps={{
                  typography: "subtitle2",
                  sx: { mb: 0.25 }
                }}
                secondaryTypographyProps={{ typography: "caption" }}
                primary={contact.name}
                secondary={contact.email}
              />
            </ListItem>
          )
        })}
      </Box>
    )}
  </DialogContent>
</Dialog>
  )
}

// ----------------------------------------------------------------------

function applyFilter({ inputData, query }) {
  if (query) {
    inputData = inputData.filter(
      contact =>
        contact.name.toLowerCase().indexOf(query.toLowerCase()) !== -1 ||
        contact.email.toLowerCase().indexOf(query.toLowerCase()) !== -1
    )
  }

  return inputData
}
