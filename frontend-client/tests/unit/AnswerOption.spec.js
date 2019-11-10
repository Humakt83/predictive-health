import { shallowMount } from '@vue/test-utils'
import AnswerOption from '@/components/AnswerOption.vue'

describe('AnswerOption.vue', () => {
  it('renders props.msg when passed', () => {
    const name = 'Test'
    const wrapper = shallowMount(AnswerOption, {
      propsData: { section: name }
    })
    expect(wrapper.find('h2').text()).toMatch(name);
  })
})
