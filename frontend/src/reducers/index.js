import { combineReducers } from 'redux';

const flashMessageEmittedReducer = (state = null, action) => {
  if (action.type === 'FLASH_MESSAGE_EMITTED') {
    return action.payload;
  }

  return state;
};

const showFlashMessageReducer = (state = false, action) => {
  if (action.type === 'FLASH_MESSAGE_EMITTED') {
    return true;
  } else if (action.type === 'HIDE_FLASH_MESSAGE') {
    return false;
  }

  return state;
};

export default combineReducers({
  flashMessage: flashMessageEmittedReducer,
  showFlashMessage: showFlashMessageReducer,
});
