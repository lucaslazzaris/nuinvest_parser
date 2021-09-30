import { shallow } from 'enzyme';
import { Link } from 'react-router-dom'
import TopBar from './TopBar';

test('Renders TopBar Component', () => {
  const wrapper = shallow(<TopBar/>);
  expect(wrapper.find(Link)).toHaveLength(1);
});