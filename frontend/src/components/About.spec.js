import { shallow } from 'enzyme';
import About from './About';

test('Renders About Component', () => {
  const wrapper = shallow(<About />);
  expect(
    wrapper.contains(
      <a href="https://www.github.com/lucaslazzaris">lucaslazzaris</a>
    )
  ).toBeTruthy();
});
