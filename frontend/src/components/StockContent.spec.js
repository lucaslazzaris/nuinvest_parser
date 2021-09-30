import { shallow } from 'enzyme';
import StockContent from './StockContent';

const stockData = [
  [
    '20/06/2021',
    'B3SA3',
    'C',
    37,
    16.31,
    603.53,
    'Easynvesting',
    '123527'
  ],
  [
    '20/06/2021',
    'VILG11',
    'V',
    30,
    115.47,
    3460.78,
    'Easynvesting',
    '123527'
  ]
];

test('Render StockContent', () => {
  const wrapper = shallow(<StockContent stockData={stockData} />);
  expect(wrapper.find({ 'data-test-id': 'stocks-row' })).toHaveLength(1);
});
