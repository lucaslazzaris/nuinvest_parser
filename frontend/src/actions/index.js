export const emitFlashMessage = (flashMessage) => {
  return {
    type: 'FLASH_MESSAGE_EMITTED',
    payload: flashMessage
  }
}

export const hideFlashMessage = () => {
  return {
    type: 'HIDE_FLASH_MESSAGE',
    payload: {}
  }
}