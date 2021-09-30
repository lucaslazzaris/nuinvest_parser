import { mount } from 'enzyme';
import { Provider } from 'react-redux';
import { MemoryRouter } from 'react-router-dom';
import { createStore } from 'redux';
import reducers from '../reducers';

const TestRouterProvider = ({ ...props }) => {
  return (
    <Provider store={testStore()}>
      <MemoryRouter {...props} />
    </Provider>
  );
};

export const testStore = (initialState) => {
  return createStore(reducers, initialState);
};

export const mountWithRouter = (ui, { route = '/' } = {}) => {
  window.history.pushState({}, 'Test page', route);

  return mount(ui, { wrappingComponent: TestRouterProvider,  attachTo: document.getElementById('container') } );
};
