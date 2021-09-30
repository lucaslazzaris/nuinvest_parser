import { shallow } from 'enzyme';
import Footer from './Footer';

test('Renders Footer Component', () => {
  const wrapper = shallow(<Footer/>);
  expect(wrapper.find(".text-muted")).toBeTruthy();
});