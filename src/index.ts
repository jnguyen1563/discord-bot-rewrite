const word = 'world';

export default function hello(world: string = word): string {
  return `Hello ${world}!`;
}
