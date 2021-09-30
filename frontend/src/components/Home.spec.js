import axios from 'axios';
import { act, Simulate } from 'react-dom/test-utils';
import { mountWithRouter, testStore } from '../helpers/testHelper';
import Home from './Home';
import StockContent from './StockContent';

jest.mock('axios');

describe('App', () => {
  beforeEach(() => {
    // Avoid `attachTo: document.body` Warning
    const div = document.createElement('div');
    div.setAttribute('id', 'container');
    document.body.appendChild(div);
  });

  afterEach(() => {
    const div = document.getElementById('container');
    if (div) {
      document.body.removeChild(div);
    }
  });

  test('Renders Home Bar', () => {
    const wrapper = mountWithRouter(<Home />);

    expect(wrapper.find(Home)).toHaveLength(1);
  });

  test('Renders the form', () => {
    const wrapper = mountWithRouter(<Home />);

    expect(wrapper.find('[data-test-id="file-form"]')).toHaveLength(1);
  });

  test('Send correct file', async () => {
    const file = new File(['(⌐□_□)'], 'chucknorris.pdf', {
      type: 'application/pdf',
    });

    const data = {
      stocks: [
        [
          '20/06/2021',
          'B3SA3',
          'C',
          37,
          16.31,
          603.53,
          'Easynvesting',
          '123527',
        ],
        [
          '20/06/2021',
          'VILG11',
          'V',
          30,
          115.47,
          3460.78,
          'Easynvesting',
          '123527',
        ],
      ],
      flash_message: { content: 'Sucesso', class: 'success' },
    };

    const wrapper = mountWithRouter(<Home />);

    await act(async () => {
      axios.post.mockResolvedValue({ data: data });

      wrapper.find('#files').simulate('change', {
        target: {
          files: [file],
        },
      });
      wrapper.update();

      Simulate.submit(wrapper.find('form').getDOMNode());
    });

    wrapper.update();

    expect(wrapper.find(StockContent)).toHaveLength(1);
    expect(wrapper.find('[data-test-id="stocks-row"]')).toHaveLength(1);
  });

  test('Do not send valid file', async () => {
    const file = new File(['(⌐□_□)'], 'chucknorris.png', {
      type: 'application/png',
    });

    const wrapper = mountWithRouter(<Home />);

    await act(async () => {
      axios.post.mockImplementation(() =>
        Promise.reject({
          response: {
            data: {
              redirect_url: '/',
              flash_message: {
                content: 'Inserir documentos no formato .pdf',
                class: 'danger',
              },
            },
          },
        })
      );

      wrapper.find('#files').simulate('change', {
        target: {
          files: [file],
        },
      });
      wrapper.update();

      Simulate.submit(wrapper.find('form').getDOMNode());
    });

    wrapper.update();

    expect(wrapper.find(StockContent)).toHaveLength(0);
    expect(wrapper.find('[data-test-id="stocks-row"]')).toHaveLength(0);
  });
});
