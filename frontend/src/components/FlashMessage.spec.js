import { testStore } from '../helpers/testHelper';
import { emitFlashMessage } from '../actions';

import { mount, shallow } from 'enzyme';
import FlashMessage from './FlashMessage';
import { act } from 'react-dom/test-utils';

describe('Flash Message', () => {
  let store;
  beforeEach(() => {
    store = testStore();
  });

  test('Renders component if message is present', () => {
    act(() => {
      store.dispatch(
        emitFlashMessage({ content: 'Sucesso', class: 'success' })
      );
    });

    const wrapper = shallow(<FlashMessage store={store} />);

    expect(
      wrapper.dive().dive().find('[data-test-id="flash-message"]')
    ).toHaveLength(1);
  });

  test('Does not render component if message is not present', () => {
    const wrapper = shallow(<FlashMessage store={store} />);

    expect(
      wrapper.dive().dive().find('[data-test-id="flash-message"]')
    ).toHaveLength(0);
  });

  test('Renders component if message is created', () => {
    const wrapper = mount(<FlashMessage store={store} />);

    act(() => {
      store.dispatch(
        emitFlashMessage({ content: 'Sucesso', class: 'success' })
      );
    });

    wrapper.update();
    expect(
      wrapper.find('[data-test-id="flash-message"]')
    ).toHaveLength(1);
  });

  test('Hides component on close button click', () => {
    act(() => {
      store.dispatch(
        emitFlashMessage({ content: 'Sucesso', class: 'success' })
      );
    });

    const wrapper = mount(<FlashMessage store={store} />);

    expect(
      wrapper.find('[data-test-id="flash-message"]')
    ).toHaveLength(1);

    act(() => {
      wrapper.find('.btn-close').simulate('click');
    });

    wrapper.update();
    expect(
      wrapper.find('[data-test-id="flash-message"]')
    ).toHaveLength(0);
  });
});
