import { alpha } from "@mui/material/styles"

export function bgBlur(props) {
  const color = props?.color || "#000000"
  const blur = props?.blur || 6
  const opacity = props?.opacity || 0.8
  const imgUrl = props?.imgUrl

  if (imgUrl) {
    return {
      position: "relative",
      backgroundImage: `url(${imgUrl})`,

      "&:before": {
        position: "absolute",
        top: 0,
        left: 0,
        zIndex: 9,
        content: '""',
        width: "100%",
        height: "100%",
        backdropFilter: `blur(${blur}px)`,
        WebkitBackdropFilter: `blur(${blur}px)`,
        backgroundColor: alpha(color, opacity)
      }
    }
  }

  return {
    backdropFilter: `blur(${blur}px)`,
    WebkitBackdropFilter: `blur(${blur}px)`,
    backgroundColor: alpha(color, opacity)
  }
}

// ----------------------------------------------------------------------

export const hideScroll = {
  x: {
    msOverflowStyle: "none",
    scrollbarWidth: "none",
    overflowX: "scroll",
    "&::-webkit-scrollbar": {
      display: "none"
    }
  },
  y: {
    msOverflowStyle: "none",
    scrollbarWidth: "none",
    overflowY: "scroll",
    "&::-webkit-scrollbar": {
      display: "none"
    }
  }
}
